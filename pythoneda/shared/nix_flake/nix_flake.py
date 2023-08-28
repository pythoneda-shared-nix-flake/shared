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
import asyncio
from pythoneda import attribute, primary_key_attribute, Entity
from pythoneda.shared.git import GitAdd, GitInit
import subprocess
import tempfile
from typing import Dict

class NixFlake(Entity):

    """
    Represents a nix flake

    Class name: NixFlake

    Responsibilities:
        - Model a nix flake.
        - Knows how to run itself.

    Collaborators:
        - None
    """
    def __init__(self, name:str, version:str, template:str, description:str):
        """
        Creates a new NixFlake instance.
        :param name: The name of the flake.
        :type name: str
        :param version: The version of the flake.
        :type version: str
        :param template: The nix flake template.
        :type template: str
        :param description: The flake description.
        :type description: str
        """
        super().__init__()
        self._name = name
        self._version = version
        self._template = template
        self._description = description
        self._inputs = {}
        self._outputs = {}

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
    def template(self) -> str:
        """
        Retrieves the template used for the flake.
        :return: Such file.
        :rtype: str
        """
        return self._template

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
    def inputs(self) -> Dict:
        """
        Retrieves the inputs of the flake.
        :return: Such collection.
        :rtype: Dict
        """
        return self._inputs

    @property
    @attribute
    def outputs(self) -> Dict:
        """
        Retrieves the outputs of the flake.
        :return: Such collection.
        :rtype: Dict
        """
        return self._outputs

    def pre_process_flake(self, flakeFolder:str):
        """
        Performs any preprocessing, if needed.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        pass

    def process_template(self, flakeFolder:str):
        """
        Processes the flake template.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        pass

    async def run(self):
        """
        Runs this flake.
        """
        with tempfile.TemporaryDirectory() as tempd:
            self.pre_process_flake(tempd)

            self.process_template(tempd)

            GitInit(tempd).init()
            GitAdd(tempd).add("flake.nix")

            try:
                process = await asyncio.create_subprocess_shell("nix run .", stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=tempFolder)
            except subprocess.CalledProcessError as err:
                print(err.stderr)

            stdout, stderr = await process.communicate()

            if stdout:
                print(stdout.decode())
            if stderr:
                print(stderr.decode())
