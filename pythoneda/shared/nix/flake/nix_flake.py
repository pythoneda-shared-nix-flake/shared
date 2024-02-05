# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/nix_flake.py

This file defines the NixFlake class.

Copyright (C) 2023-today rydnr's pythoneda-shared-nix-flake/shared

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from .fetch_sha256_failed import FetchSha256Failed
from .flake_lock_update_failed import FlakeLockUpdateFailed
import json
import os
from .license import License
from .nix_flake_input import NixFlakeInput
from pathlib import Path
from pythoneda.shared import attribute, primary_key_attribute, Entity
from pythoneda.shared.git import GitAdd, GitInit
from pythoneda.shared.shell import AsyncShell
import re
from stringtemplate3 import PathGroupLoader, StringTemplateGroup
import subprocess
import tempfile
from typing import Callable, List


class NixFlake(Entity):

    """
    Represents a Nix flake.

    Class name: NixFlake

    Responsibilities:
        - Model a Nix flake.
        - Knows how to run itself.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlakeInput
    """

    def __init__(
        self,
        name: str,
        version: str,
        urlFor: Callable[[str], str],
        inputs: List,
        templateSubfolder: str,
        description: str,
        homepage: str,
        licenseId: str,
        maintainers: List,
        copyrightYear: int,
        copyrightHolder: str,
        templatesFolder: str = None,
    ):
        """
        Creates a new NixFlake instance.
        :param name: The name of the flake.
        :type name: str
        :param version: The version of the flake.
        :type version: str
        :param urlFor: The function to obtain the url from a given version.
        :type urlFor: Callable[[str],str]
        :param inputs: The flake inputs.
        :type inputs: List[pythoneda.shared.nix.flake.NixFlakeInput]
        :param templateSubfolder: The template subfolder, if any.
        :type templateSubfolder: str
        :param description: The flake description.
        :type description: str
        :param homepage: The project's homepage.
        :type homepage: str
        :param licenseId: The id of the license of the project.
        :type licenseId: str
        :param maintainers: The maintainers of the project.
        :type maintainers: List[str]
        :param copyrightYear: The copyright year.
        :type copyrightYear: year
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        :param templatesFolder: The folder with the templates.
        :type templatesFolder: str
        """
        super().__init__()
        self._name = name
        self._version = version
        self._url_for = urlFor
        self._inputs = list({obj.name: obj.to_input() for obj in inputs}.values())
        self._template_subfolder = templateSubfolder
        self._description = description
        self._homepage = homepage
        self._license = License.from_id(
            licenseId, copyrightYear, copyrightHolder, homepage
        )
        self._maintainers = maintainers
        self._copyright_year = copyrightYear
        self._copyright_holder = copyrightHolder
        if templatesFolder:
            self._templates_folder = templatesFolder
        else:
            self._templates_folder = self.default_templates_folder()

        for bindable_input in self._inputs:
            bindable_input.bind(self)

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.nix.flake.NixFlake
        """
        return cls(None, None, None, [], None, None, None, None, [], None, None)

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name of the flake.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    @primary_key_attribute
    def version(self) -> str:
        """
        Retrieves the version of the flake.
        :return: Such version.
        :rtype: str
        """
        return self._version

    @property
    @primary_key_attribute
    def url_for_function(self) -> Callable[[str], str]:
        """
        Retrieves the function to obtain the url of the flake from a given version.
        :return: Such function.
        :rtype: Callable[[str],str]
        """
        return self._url_for

    @property
    @attribute
    def inputs(self) -> List:
        """
        Retrieves the inputs of the flake.
        :return: Such collection.
        :rtype: List
        """
        return self._inputs

    def update_input(self, target: NixFlakeInput) -> bool:
        """
        Updates given input.
        :param target: The input to update.
        :type target: pythoneda.shared.nix.flake.NixFlakeInput
        :return: True if the input was found and updated; False otherwise.
        :rtype: bool
        """
        result = False
        for i, item in enumerate(self.inputs):
            if item.url == target.url:
                self.inputs[i] = target
                result = True
                break
        return result

    def remove_input(self, target: NixFlakeInput) -> bool:
        """
        Removes given input.
        :param target: The input to remove.
        :type target: pythoneda.shared.nix.flake.NixFlakeInput
        :return: True if the input was found and removed; False otherwise.
        :rtype: bool
        """
        result = False
        if target in self.inputs:
            self.inputs.remove(target)
            result = True
        return result

    def add_input(self, target: NixFlakeInput) -> bool:
        """
        Adds given input.
        :param target: The input to add.
        :type target: pythoneda.shared.nix.flake.NixFlakeInput
        :return: True if the input was not found and added; False otherwise.
        :rtype: bool
        """
        result = False
        if target not in self.inputs:
            self.inputs.append(target)
            result = True
        return result

    @property
    @attribute
    def template_subfolder(self) -> str:
        """
        Retrieves the template subfolder, if any.
        :return: Such subfolder.
        :rtype: str
        """
        return self._template_subfolder

    @property
    @attribute
    def description(self) -> str:
        """
        Retrieves the flake description.
        :return: Such description.
        :rtype: str
        """
        return self._description

    @property
    @attribute
    def license(self) -> str:
        """
        Retrieves the project license.
        :return: Such information.
        :rtype: str
        """
        return self._license

    @property
    def license_text(self) -> str:
        """
        Retrieves the text of the license.
        :return: Such information.
        :rtype: str
        """
        return self._license.preamble

    @property
    def license_text_with_hash(self) -> str:
        """
        Retrieves the text of the license with a hash prefix.
        :return: Such information.
        :rtype: str
        """
        return self.with_prefix(self.license_text, "#")

    @property
    def license_text_with_double_slash(self) -> str:
        """
        Retrieves the text of the license with a double slash prefix.
        :return: Such information.
        :rtype: str
        """
        return self.with_prefix(self.license_text, "//")

    def with_prefix(self, text: str, prefix: str) -> str:
        """
        Retrieves given text with given prefix.
        :param text: The text to process.
        :type text: str
        :param prefix: The prefix to add to each line.
        :type prefix: str
        :return: Such information.
        :rtype: str
        """
        return "\n".join([f"{prefix}{line}" for line in text.split("\n")])

    @property
    def license_id(self) -> str:
        """
        Retrieves the id of the license.
        :return: Such information.
        :rtype: str
        """
        return self._license.license_id

    @property
    @attribute
    def maintainers(self) -> List[str]:
        """
        Retrieves the project maintainers.
        :return: Such information.
        :rtype: List[str]
        """
        return self._maintainers

    @property
    @attribute
    def copyright_year(self) -> int:
        """
        Retrieves the copyright year.
        :return: Such information.
        :rtype: int
        """
        return self._copyright_year

    @property
    @attribute
    def copyright_holder(self) -> int:
        """
        Retrieves the copyright holder.
        :return: Such information.
        :rtype: str
        """
        return self._copyright_holder

    @property
    @attribute
    def homepage(self) -> str:
        """
        Retrieves the project's homepage.
        :return: Such url.
        :rtype: str
        """
        return self._homepage

    @property
    def templates_folder(self) -> str:
        """
        Retrieves the templates folder.
        :return: Such folder.
        :rtype: str
        """
        return self._templates_folder

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == "inputs":
            self._inputs = [NixFlakeInput.from_dict(value) for value in varValue]
            for input in self._inputs:
                input.bind(self)
        elif varName == "license":
            if varValue is not None:
                self._license = License.from_dict(varValue)
        else:
            super()._set_attribute_from_json(varName, varValue)

    def _get_attribute_to_json(self, varName) -> str:
        """
        Retrieves the value of an attribute of this instance, as Json.
        :param varName: The name of the attribute.
        :type varName: str
        :return: The attribute value in json format.
        :rtype: str
        """
        result = None
        if varName == "inputs":
            result = [aux.to_dict() for aux in self._inputs]

        elif varName == "license":
            if self._license is None:
                result = None
            else:
                result = self._license.to_dict()
        else:
            result = super()._get_attribute_to_json(varName)
        return result

    async def generate_files(self, flakeFolder: str):
        """
        Generates the files.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        await self.generate_flake(flakeFolder)

    def parent_folder(self, path: str) -> str:
        """
        Retrieves the parent folder of given path.
        :param path: The path.
        :type path: str
        :return: The parent folder.
        :rtype: str
        """
        return os.path.dirname(path)

    def default_templates_folder(self) -> str:
        """
        Retrieves the default templates folder.
        :return: Such location.
        :rtype: str
        """
        return (
            Path(
                self.parent_folder(
                    self.parent_folder(
                        self.parent_folder(
                            self.parent_folder(self.parent_folder(__file__))
                        )
                    )
                )
            )
            / "templates"
        )

    def to_input(self) -> NixFlakeInput:
        """
        Converts this flake to an input for other flake.
        :return: The input.
        :rtype: pythoneda.shared.nix.flake.NixFlakeInput
        """
        return NixFlakeInput(self.name, self.version, self.url_for, self.inputs)

    async def generate_flake(self, flakeFolder: str) -> str:
        """
        Generates the flake from a template.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        :return: The generated flake.nix file.
        :rtype: str
        """
        await self.process_template(
            flakeFolder,
            "FlakeNix",
            Path(self.templates_folder) / self.template_subfolder,
            "root",
            "flake.nix",
        )
        return Path(flakeFolder) / "flake.nix"

    async def process_template(
        self,
        outputFolder: str,
        groupName: str,
        templateFolder: str,
        rootTemplate: str,
        outputFileName: str,
    ):
        """
        Processes a template.
        :param outputFolder: The output folder.
        :type outputFolder: str
        :param groupName: The name of the stringtemplate group.
        :type groupName: str
        :param templateFolder: The subfolder with the templates.
        :type templateFolder: str
        :param rootTemplate: The root template.
        :type rootTemplate: str
        :param outputFileName: The name of the generated file.
        :type outputFileName: str
        """
        # Manually read the .stg file
        with open(
            Path(templateFolder) / f"{groupName}.stg", "r", encoding="utf-8"
        ) as f:
            # Create a group from the string content
            group = StringTemplateGroup(
                name=groupName, file=f, rootDir=str(templateFolder)
            )

            root_template = group.getInstanceOf("root")
            root_template["flake"] = self

        with open(Path(outputFolder) / outputFileName, "w") as output_file:
            output_file.write(str(root_template))

    async def git_add_files(self, gitAdd):
        """
        Adds the generated files to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        await self.git_add_flake(gitAdd)

    async def git_add_flake(self, gitAdd):
        """
        Adds the generated flake.nix file to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        await gitAdd.add("flake.nix")

    async def run(self) -> str:
        """
        Runs this flake, and returns the path to the derivation.
        :return: Such path.
        :rtype: str
        """
        result = None
        with tempfile.TemporaryDirectory() as tmp_folder:
            await self.generate_files(tmp_folder)
            await GitInit(tmp_folder).init()
            await self.git_add_files(GitAdd(tmp_folder))

            NixFlake.logger().debug(f'Launching "nix run" on {tmp_folder}')
            process, _, _ = await AsyncShell(
                ["command", "nix", "run", "."], tmp_folder
            ).run()

            result = await self.eval(tmp_folder)

        NixFlake.logger().debug(f'"nix run" finished: {result}')

        return result

    async def eval(self, path: str) -> str:
        """
        Runs "nix eval ." in given folder,
        :return: The path of the derivation.
        :rtype: str
        """
        process, _, _ = await AsyncShell(["command", "nix", "eval", "."], path)

        return process.stdout

    @classmethod
    async def update_flake_lock(cls, repositoryFolder: str, flakeSubfolder: str = None):
        """
        Updates the flake.lock file.
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
        :param flakeSubfolder: The subfolder of the flake.nix file.
        :type flakeSubfolder: str
        """
        subfolder = "."
        if flakeSubfolder is not None:
            subfolder = f"{flakeSubfolder}/"

        process, stdout, stderr = await AsyncShell(
            ["command", "nix", "flake", "update", subfolder], repositoryFolder
        ).run()

        if process.returncode != 0:
            if stdout != "":
                NixFlake.logger().debug(stdout)
            if stderr != "":
                NixFlake.logger().error(stderr)
                raise FlakeLockUpdateFailed(repositoryFolder, subfolder, stderr)

        return True

    @classmethod
    async def fetch_sha256(cls, url: str, rev: str) -> str:
        """
        Retrieves the sha256 checksum for given url.
        :param url: The repository url.
        :type url: str
        :param rev: The revision.
        :type rev: str
        :return: The sha256 value.
        :rtype: str
        """
        result = None

        with tempfile.TemporaryDirectory() as temp_dir:
            process, stdout, stderr = await AsyncShell(
                ["nix-prefetch-git", "--quiet", url, "--rev", rev]
            ).run()

            if process.returncode == 0:
                result = json.loads(stdout).get("sha256", None)

            if result is None:
                raise FetchSha256Failed(url, rev, stderr)

        return result

    @classmethod
    async def update_sha256(
        cls, sha256: str, repositoryFolder: str, flakeSubfolder: str = None
    ):
        """
        Updates the sha256 checksum in the flake.nix file.
        :param sha256: The sha256 checksum.
        :type sha256: str
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
        :param flakeSubfolder: The subfolder of the flake.nix file.
        :type flakeSubfolder: str
        """
        folder = repositoryFolder

        if flakeSubfolder is not None:
            folder = os.path.join(folder, flakeSubfolder)

        # Regular expression pattern to match the sha256 line
        sha256_pattern = r'(sha256\s*=\s*")[^"]*(";)'

        flake_nix = os.path.join(folder, "flake.nix")
        # Read the file contents
        with open(flake_nix, "r") as file:
            file_contents = file.read()

            # Replace the sha256 value using regular expression
            updated_contents = re.sub(
                sha256_pattern, r"\g<1>" + sha256 + r"\2", file_contents
            )

        # Write the updated contents back to the file
        with open(flake_nix, "w") as file:
            file.write(updated_contents)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
