"""
pythoneda/shared/nix_flake/nix_flake.py

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
from .nix_flake_input import NixFlakeInput
import asyncio
import os
from pathlib import Path
from pythoneda import attribute, primary_key_attribute, Entity
from pythoneda.shared.git import GitAdd, GitInit
from pythoneda.shared.nix_flake import License
from stringtemplate3 import PathGroupLoader, StringTemplateGroup
import subprocess
import tempfile
from typing import Dict, List

class NixFlake(Entity):

    """
    Represents a Nix flake.

    Class name: NixFlake

    Responsibilities:
        - Model a Nix flake.
        - Knows how to run itself.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlakeInput
    """
    def __init__(
            self,
            name:str,
            version:str,
            url:str,
            inputs:List,
            templateSubfolder:str,
            description:str,
            homepage:str,
            licenseId:str,
            maintainers:List,
            copyrightYear:int,
            copyrightHolder:str):
        """
        Creates a new NixFlake instance.
        :param name: The name of the flake.
        :type name: str
        :param version: The version of the flake.
        :type version: str
        :param url: The url of the Nix flake.
        :type url: str
        :param inputs: The flake inputs.
        :type inputs: List[pythoneda.shared.nix_flake.NixFlakeInput]
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
        """
        super().__init__()
        self._name = name
        self._version = version
        self._url = url
        self._inputs = list({obj.name: obj.to_input() for obj in inputs}.values())
        self._template_subfolder = templateSubfolder
        self._description = description
        self._homepage = homepage
        self._license = License.from_id(licenseId, copyrightYear, copyrightHolder, homepage)
        self._maintainers = maintainers
        self._copyright_year = copyrightYear
        self._copyright_holder = copyrightHolder
        for input in self._inputs:
            input.bind(self)

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.ValueObject
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
    def url(self) -> str:
        """
        Retrieves the url of the flake.
        :return: Such url.
        :rtype: str
        """
        return self._url

    @property
    @attribute
    def inputs(self) -> List:
        """
        Retrieves the inputs of the flake.
        :return: Such collection.
        :rtype: List
        """
        return self._inputs

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

    def with_prefix(self, text:str, prefix:str) -> str:
        """
        Retrieves given text with given prefix.
        :param text: The text to process.
        :type text: str
        :param prefix: The prefix to add to each line.
        :type prefix: str
        :return: Such information.
        :rtype: str
        """
        return '\n'.join([f'{prefix}{line}' for line in text.split('\n')])

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

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == 'inputs':
            self._inputs = [NixFlakeInput.from_dict(value) for value in varValue]
            for input in self._inputs:
                input.bind(self)
        elif varName == 'license':
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
        if varName == 'inputs':
            result = [input.to_dict() for input in self._inputs]

        elif varName == 'license':
            if self._license is None:
                result = None
            else:
                result = self._license.to_dict()
        else:
            result = super()._get_attribute_to_json(varName)
        return result

    def generate_files(self, flakeFolder:str):
        """
        Generates the files.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        self.generate_flake(flakeFolder)

    def parent_folder(self, path:str) -> str:
        """
        Retrieves the parent folder of given path.
        :param path: The path.
        :type path: str
        :return: The parent folder.
        :rtype: str
        """
        return os.path.dirname(path)

    def templates_folder(self) -> str:
        """
        Retrieves the templates folder.
        :return: Such location.
        :rtype: str
        """
        return Path(self.parent_folder(self.parent_folder(self.parent_folder(self.parent_folder(__file__))))) / "templates"

    def to_input(self) -> NixFlakeInput:
        """
        Converts this flake to an input for other flake.
        :return: The input.
        :rtype: pythoneda.shared.nix_flake.NixFlakeInput
        """
        return NixFlakeInput(self.name, self.url, self.inputs)

    def generate_flake(self, flakeFolder:str):
        """
        Generates the flake from a template.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        self.process_template(flakeFolder, "FlakeNix", Path(self.templates_folder()) / self.template_subfolder, "root", "flake.nix")

    def process_template(self, outputFolder:str, groupName:str, templateFolder:str, rootTemplate:str, outputFileName:str):
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
        with open(Path(templateFolder) / f"{groupName}.stg", 'r', encoding='utf-8') as f:

            # Create a group from the string content
            group = StringTemplateGroup(name=groupName, file=f, rootDir=str(templateFolder))

            root_template = group.getInstanceOf("root")
            root_template["flake"] = self

        with open(Path("/tmp/debug") / outputFileName, "w") as output_file:
            output_file.write(str(root_template))

        with open(Path(outputFolder) / outputFileName, "w") as output_file:
            output_file.write(str(root_template))

    def git_add_files(self, gitAdd):
        """
        Adds the generated files to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        self.git_add_flake(gitAdd)

    def git_add_flake(self, gitAdd):
        """
        Adds the generated flake.nix file to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        gitAdd.add("flake.nix")

    async def run(self) -> str:
        """
        Runs this flake, and returns the path to the derivation.
        :return: Such path.
        :rtype: str
        """
        result = None
        with tempfile.TemporaryDirectory() as tmp_folder:
            self.generate_files(tmp_folder)
            GitInit(tmp_folder).init()
            self.git_add_files(GitAdd(tmp_folder))

            NixFlake.logger().debug(f'Launching "nix run" on {tmp_folder}')
            try:
                process = await asyncio.create_subprocess_shell(
                    "nix run .",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=tmp_folder,
                    bufsize=0,
                    universal_newlines=False,
                    env={'PATH': os.environ['PATH']})

                async def read_stream(stream, callback):
                    while True:
                        line = await stream.readline()
                        if line:
                            callback(line)
                        else:
                            break

                def print_stdout(line:str):
                    print(line.decode().rstrip())

                def print_stderr(line:str):
                    NixFlake.logger().info(line.decode().rstrip())

                await asyncio.gather(
                    read_stream(process.stdout, print_stdout),
                    read_stream(process.stderr, print_stderr))

                await process.wait()

                result = await self.eval(tmp_folder)

            except subprocess.CalledProcessError as err:
                NixFlake.logger().error(err.stderr)

        NixFlake.logger().debug(f'"nix run" finished: {result}')

        return result

    async def eval(self, path:str) -> str:
        """
        Runs "nix eval ." in given folder,
        :return: The path of the derivation.
        :rtype: str
        """
        result = None
        try:
            execution = subprocess.run(
                ["nix", "eval", "."],
                check=True,
                capture_output=True,
                text=True,
                cwd=path,
            )
            result = execution.stdout
        except subprocess.CalledProcessError as err:
            NixFlake.logger().error(err)
            NixFlake.logger().error(err.stderr)

        return result
