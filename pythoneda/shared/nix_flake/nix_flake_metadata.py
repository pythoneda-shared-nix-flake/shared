"""
pythoneda/shared/nix_flake/nix_flake_metadata.py

This file defines the NixFlakeMetadata class.

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
from .github_url_for import GithubUrlFor
import json
from .nix_flake_input import NixFlakeInput
from pythoneda import attribute, Entity
import re
import subprocess
from typing import Dict, List


class NixFlakeMetadata(Entity):

    """
    Represents Nix flake metadata.

    Class name: NixFlakeMetadata

    Responsibilities:
        - Extract metadata information from `nix flake metadata`

    Collaborators:
        - None
    """

    def __init__(self, metadata: Dict, flakeFolder: str):
        """
        Creates a new NixFlakeMetadata instance.
        :param metadata: The flake folder.
        :type metadata: Dict
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        super().__init__()
        self._metadata = metadata
        self._flake_folder = flakeFolder

    @property
    @attribute
    def metadata(self) -> Dict:
        """
        Retrieves the metadata.
        :return: Such metadata.
        :rtype: Dict
        """
        return self._metadata

    @property
    @attribute
    def flake_folder(self) -> str:
        """
        Retrieves the flake folder.
        :return: Such folder.
        :rtype: str
        """
        return self._flake_folder

    @classmethod
    def from_folder(cls, flakeFolder: str):
        """
        Retrieves the license for given id, customized for given copyright information.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        :return: The metadata, of None if it could not be extracted.
        :rtype: pythoneda.shared.nix_flake.NixFlakeMetadata
        """
        result = None

        command = f"nix flake metadata --json {flakeFolder}"
        execution = subprocess.run(command, shell=True, capture_output=True, text=True)
        if execution.returncode != 0:
            raise Exception(f"Error running command: {execution.stderr}")
        return cls(json.loads(execution.stdout), flakeFolder)

    def url(self) -> str:
        """
        Retrieves the url of the flake.
        :return: The url, if available.
        :rtype: str
        """
        return self.metadata.get("locked", None).get("url", None)

    def inputs(self) -> List:
        """
        Retrieves the flake inputs.
        :return: Such inputs.
        :rtype: List
        """
        deps = self.metadata.get("locks", {}).get("nodes", {})
        items = deps.items()
        result = []
        node_versions = {}
        for node, details in deps.get("root", {}).get("inputs", {}).items():
            result.append(self._to_input(node))

        return result

    def _find_input_details(self, node: str) -> Dict:
        """
        Retrieves the details of given input.
        :param node: The node.
        :type node: str
        :return: The node details.
        :rtype: Dict
        """
        return self.metadata.get("locks", {}).get("nodes", {}).get(node, {})

    def indirect_inputs(self) -> Dict[str, NixFlakeInput]:
        """
        Retrieves all inputs.
        :return: A dictionary with the name as key and the input as value.
        :rtype: Dict[str, NixFlakeInput]
        """
        return [
            self._to_input(node)
            for node in self.metadata.get("locks", {}).get("nodes", {})
            if node != "root"
        ]

    def _to_input(self, node: str) -> NixFlakeInput:
        """
        Converts given information into a NixFlakeInput.
        :param node: The node name.
        :type node: str
        :return: The Nix flake input.
        :rtype: pythoneda.shared.nix_flake.NixFlakeMetadata
        """
        result = None
        data = (
            self.metadata.get("locks", {})
            .get("nodes", {})
            .get(node, {})
            .get("original", {})
        )
        if data.get("type", None) == "github":
            owner = data["owner"]
            repo = data["repo"]
            version = data["ref"]
            dir = data.get("dir", None)

            inputs = self._get_inputs(node)

            result = NixFlakeInput(
                node,
                version,
                GithubUrlFor(owner, repo, dir).url_for,
                inputs,
            )
        return result

    def _get_inputs(self, node: str) -> List[NixFlakeInput]:
        """
        Retrieves the inputs of given node.
        :param node: The node name.
        :type node: str
        :return: The node's inputs, if any.
        :rtype: List
        """
        result = []
        details = self._find_input_details(node)
        for dep, contents in details.get("inputs", {}).items():
            if isinstance(contents, str):
                result.append(self._to_input(contents))
            else:
                result.append(self._to_input(dep))
        return result

    def duplicated_inputs(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of duplicated inputs.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        result = []
        input_versions = {}
        for input in self.inputs():
            normalized_name = self.normalized_input_name(input)
            input_versions[normalized_name] = input.version
            input_versions[input.name] = input.version
        for input in self.indirect_inputs():
            normalized_name = self.normalized_input_name(input)
            if input_versions.get(normalized_name, None) is None:
                input_versions[normalized_name] = input.version
            else:
                result.append(input)
            input_versions[input.name] = input.version
        return result

    def inputs_with_duplicates(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of direct inputs with duplicates.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        result = []
        input_versions = {}
        for input in self.inputs():
            normalized_name = self.normalized_input_name(input)
            input_versions[normalized_name] = input.version
            input_versions[input.name] = input.version
        for input in self.indirect_inputs():
            normalized_name = self.normalized_input_name(input)
            if input_versions.get(normalized_name, None) is None:
                input_versions[normalized_name] = input.version
            else:
                result.append(self._to_input(normalized_name))
            input_versions[input.name] = input.version
        return result

    def normalized_input_name(self, input: NixFlakeInput) -> str:
        """
        Normalizes the name of given input, according to Nix flake conventions.
        :param input: The input.
        :type input: pythoneda.shared.nix_flake.NixFlakeInput
        :return: The normalized name.
        :rtype: str
        """
        return re.sub(r"_\d+$", "", input.name)

    def all_inputs(self) -> List[NixFlakeInput]:
        """
        Retrieves all inputs.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        result = []
        [
            result.append(item)
            for item in self.inputs() + self.indirect_inputs()
            if item not in result
        ]
        return result

    def get_duplicates(self, input: NixFlakeInput) -> List[NixFlakeInput]:
        """
        Retrieves the duplicates of given input.
        :param input: The input.
        :type input: pythoneda.shared.nix_flake.NixFlakeInput
        :return: The list of duplicates.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        result = []
        for candidate in self.all_inputs():
            if input != candidate and self.normalized_input_name(
                input
            ) == self.normalized_input_name(candidate):
                result.append(candidate)

        return result

    def has_duplicates(self, input: NixFlakeInput) -> bool:
        """
        Checks if given input has duplicates with different version.
        :param input: The input.
        :type input: pythoneda.shared.nix_flake.NixFlakeInput
        :return: True in such case.
        :rtype: bool
        """
        return len(self.get_duplicates(input)) > 0

    def has_duplicates_with_different_version(self, input: NixFlakeInput) -> bool:
        """
        Checks if given input has duplicates with different version.
        :param input: The input.
        :type input: pythoneda.shared.nix_flake.NixFlakeInput
        :return: True in such case.
        :rtype: bool
        """
        result = False
        for candidate in self.get_duplicates(input):
            if candidate.version != input.version:
                result = True
                break

        return result
