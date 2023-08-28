"""
pythoneda/shared/nix_flake/python/pyproject_nix_flake.py

This file defines the PyprojectNixFlake class.

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
from enum import Enum
from pythoneda import attribute, primary_key_attribute
from pythoneda.shared.nix_flake import NixFlake
from typing import Dict

class PyprojectNixFlake(NixFlake):

    """
    Represents a nix flake using to build a pyproject-based Python package.

    Class name: PyprojectNixFlake

    Responsibilities:
        - Model a nix flake for a pyproject-based Python package.
        - Knows how to run itself.

    Collaborators:
        - pythoneda.shared.code_requests.nix_flake.NixFlake
    """
    def __init__(self, name:str, version:str, description:str):
        """
        Creates a new PyprojectNixFlake instance.
        :param name: The name of the flake.
        :type name: str
        :param version: The version of the flake.
        :type version: str
        :param description: The flake description.
        :type description: str
        """
        super().__init__(name, version, "pyproject-flake.nix.template", description)

    class Subtemplates(Enum):
        INPUTS = "inputs"
        FLAKE_DEPENDENCIES_AS_INPUTS = "flake_dependencies_as_inputs"
        FLAKE_DEPENDENCIES_AS_PARAMETER_DECLARATION = "flake_dependencies_as_parameter_declaration"
        FLAKE_DEPENDENCIES_VERSION_PYPROJECT_DECLARATION = "flake_dependencies_version_pyproject_declaration"
        FLAKE_DEPENDENCIES_AS_BUILD_INPUTS = "flake_dependencies_as_build_inputs"
        FLAKE_DEPENDENCIES_AS_PARAMETERS_FOR_PYTHON38 = "flake_dependencies_as_parameters_for_python38"
        FLAKE_DEPENDENCIES_AS_PARAMETERS_FOR_PYTHON39 = "flake_dependencies_as_parameters_for_python39"
        FLAKE_DEPENDENCIES_AS_PARAMETERS_FOR_PYTHON310 = "flake_dependencies_as_parameters_for_python310"
        PYTHONEDA_FLAKE_PARAMETER = "pythoneda_flake_parameter"

    def process_inputs(self) -> str:
        """
        Processes the inputs subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pass

    def process_flake_dependencies_as_inputs(self) -> str:
        """
        Processes the flake_dependencies_as_inputs subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pass

    def process_flake_dependencies_as_parameter_declaration(self) -> str:
        """
        Processes the flake_dependencies_as_parameter_declaration subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pass

    def process_flake_dependencies_version_pyproject_declaration(self) -> str:
        """
        Processes the flake_dependencies_version_pyproject_declaration subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pass

    def process_flake_dependencies_as_build_inputs(self) -> str:
        """
        Processes the flake_dependencies_as_build_inputs subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pass

    def process_flake_dependencies_as_parameters_for_python38(self) -> str:
        """
        Processes the flake_dependencies_as_parameters_for_python38 subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pieces = []
        for dep in self.dependencies():
            pieces.append(self.process_pythoneda_flake_parameter(dep, "39"))
        return "".join(pieces)

    def process_flake_dependencies_as_parameters_for_python39(self) -> str:
        """
        Processes the flake_dependencies_as_parameters_for_python39 subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pieces = []
        for dep in self.dependencies():
            pieces.append(self.process_pythoneda_flake_parameter(dep, "39"))
        return "".join(pieces)

    def process_flake_dependencies_as_parameters_for_python310(self) -> str:
        """
        Processes the flake_dependencies_as_parameters_for_python310 subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pieces = []
        for dep in self.dependencies():
            pieces.append(self.process_pythoneda_flake_parameter(dep, "310"))
        return "".join(pieces)

    def process_pythoneda_flake_parameter(self, dependency:str, pythonVersion:str) -> str:
        """
        Processes the pythoneda_flake_parameter subtemplate.
        :return: The resulting text.
        :rtype: str
        """
        pass

    def process_template(self, flakeFolder:str) -> str:
        """
        Processes the flake template.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        :return: The resulting text.
        :rtype: str
        """
        # placeholders:
        # name
        # version
        # pythoneda_shared_pythoneda_banner_version
        pass
