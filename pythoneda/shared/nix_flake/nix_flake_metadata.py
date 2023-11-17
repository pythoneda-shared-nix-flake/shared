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
from .nix_flake_input_relationship import NixFlakeInputRelationship
from pythoneda import attribute, Entity
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

    def __init__(self, metadata: Dict, flakeRef: str):
        """
        Creates a new NixFlakeMetadata instance.
        :param metadata: The flake metadata.
        :type metadata: Dict
        :param flakeRef: The flake reference (either a folder or an url).
        :type flakeRef: str
        """
        super().__init__()
        self._metadata = metadata
        self._flake_ref = flakeRef
        self._inputs = None
        self._input_versions = None
        self._indirect_inputs = None
        self._all_inputs = None
        self._inputs_of_node = {}
        self._inputs_by_node = {}
        self._duplicated_inputs = None
        self._inputs_with_no_duplicates = None
        self._inputs_with_duplicates = None
        self._inputs_with_duplicates_with_same_version = None
        self._inputs_with_duplicates_with_different_versions = None
        self._indirect_inputs_with_no_duplicates = None
        self._indirect_inputs_with_duplicates = None
        self._indirect_inputs_with_duplicates_with_same_version = None
        self._indirect_inputs_with_duplicates_with_different_versions = None
        self._all_relationships = None
        self._relationships_for_duplicated_nodes = None

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
    def flake_ref(self) -> str:
        """
        Retrieves the flake reference.
        :return: Such reference (either a folder or an url).
        :rtype: str
        """
        return self._flake_ref

    @classmethod
    def from_ref(cls, flakeRef: str):
        """
        Creates a new instance using given flake reference.
        :param flakeRef: The flake reference (a folder or an url).
        :type flakeRef: str
        :return: The metadata, of None if it could not be extracted.
        :rtype: pythoneda.shared.nix_flake.NixFlakeMetadata
        """
        result = None

        command = f"nix flake metadata --json {flakeRef}"
        execution = subprocess.run(command, shell=True, capture_output=True, text=True)
        if execution.returncode != 0:
            raise Exception(f"Error running command: {execution.stderr}")
        return cls(json.loads(execution.stdout), flakeRef)

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
        if self._inputs is None:
            self._inputs = []
            for node, details in (
                self.metadata.get("locks", {})
                .get("nodes", {})
                .get("root", {})
                .get("inputs", {})
                .items()
            ):
                self._inputs.append(self._to_input(node))

        return self._inputs

    def _find_input_details(self, node: str) -> Dict:
        """
        Retrieves the details of given input.
        :param node: The node.
        :type node: str
        :return: The node details.
        :rtype: Dict
        """
        return self.metadata.get("locks", {}).get("nodes", {}).get(node, {})

    def indirect_inputs(self) -> List[NixFlakeInput]:
        """
        Retrieves the indirect inputs.
        :return: A list with the indirect inputs.
        :rtype: List[NixFlakeInput]
        """
        if self._indirect_inputs is None:
            root_inputs = list(
                self.metadata.get("locks", {})
                .get("nodes", {})
                .get("root", {})
                .get("inputs", {})
                .keys()
            )
            self._indirect_inputs = [
                self._to_input(node)
                for node, _ in self.metadata.get("locks", {}).get("nodes", {}).items()
                if node is not None and node not in root_inputs
            ]
            self._indirect_inputs = [
                input for input in self._indirect_inputs if input is not None
            ]
        return self._indirect_inputs

    def _to_input(self, node: str) -> NixFlakeInput:
        """
        Converts given information into a NixFlakeInput.
        :param node: The node name.
        :type node: str
        :return: The Nix flake input.
        :rtype: pythoneda.shared.nix_flake.NixFlakeMetadata
        """
        result = self._inputs_by_node.get(node, None)
        if result is None:
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
                self._inputs_by_node[node] = result
        return result

    def _get_inputs(self, node: str) -> List[NixFlakeInput]:
        """
        Retrieves the inputs of given node.
        :param node: The node name.
        :type node: str
        :return: The node's inputs, if any.
        :rtype: List
        """
        result = self._inputs_of_node.get(node, None)
        if result is None:
            result = []
            details = self._find_input_details(node)
            for dep, contents in details.get("inputs", {}).items():
                if isinstance(contents, str):
                    result.append(self._to_input(contents))
                else:
                    result.append(self._to_input(dep))
            self._inputs_of_node[node] = result
        return result

    def _process_all_inputs(self):
        """
        Processes all inputs.
        """
        if self._input_versions is None:
            self._input_versions = {}
            for input in self.inputs():
                normalized_name = input.normalized_name
                self._input_versions[normalized_name] = input.version
                self._input_versions[input.name] = input.version
            for input in self.indirect_inputs():
                normalized_name = input.normalized_name
                if self._input_versions.get(normalized_name, None) is None:
                    self._input_versions[normalized_name] = input.version
                self._input_versions[input.name] = input.version

    def duplicated_inputs(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of duplicated inputs.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._duplicated_inputs is None:
            self._duplicated_inputs = []
            self._process_all_inputs()
            self._input_versions = {}
            for input in self.all_inputs():
                if self.has_duplicates(input):
                    self._duplicated_inputs.append(input)
        return self._duplicated_inputs

    def inputs_with_no_duplicates(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of direct inputs with no duplicates.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._inputs_with_no_duplicates is None:
            duplicated_inputs = self.duplicated_inputs()
            self._inputs_with_no_duplicates = [
                input for input in self.inputs() if input not in duplicated_inputs
            ]
        return self._inputs_with_no_duplicates

    def inputs_with_duplicates(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of direct inputs with duplicates.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._inputs_with_duplicates is None:
            duplicated_inputs = self.duplicated_inputs()
            self._inputs_with_duplicates = [
                input for input in self.inputs() if input in duplicated_inputs
            ]
        return self._inputs_with_duplicates

    def inputs_with_duplicates_with_same_version(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of direct inputs with duplicates, sharing the same version.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._inputs_with_duplicates_with_same_version is None:
            inputs_with_duplicates = self.inputs_with_duplicates()
            self._inputs_with_duplicates_with_same_version = [
                input
                for input in inputs_with_duplicates
                if self.has_duplicates_with_same_version(input)
            ]
        return self._inputs_with_duplicates_with_same_version

    def inputs_with_duplicates_with_different_versions(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of direct inputs with duplicates, with different versions.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._inputs_with_duplicates_with_different_versions is None:
            inputs_with_duplicates = self.inputs_with_duplicates()
            self._inputs_with_duplicates_with_different_versions = [
                input
                for input in inputs_with_duplicates
                if self.has_duplicates_with_different_versions(input)
            ]
        return self._inputs_with_duplicates_with_different_versions

    def indirect_inputs_with_no_duplicates(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of indirect inputs with no duplicates.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._indirect_inputs_with_no_duplicates is None:
            duplicated_inputs = self.duplicated_inputs()
            self._indirect_inputs_with_no_duplicates = [
                input
                for input in self.indirect_inputs()
                if input not in duplicated_inputs
            ]
        return self._indirect_inputs_with_no_duplicates

    def indirect_inputs_with_duplicates(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of indirect inputs with duplicates.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._indirect_inputs_with_duplicates is None:
            duplicated_inputs = self.duplicated_inputs()
            self._indirect_inputs_with_duplicates = [
                input for input in self.indirect_inputs() if input in duplicated_inputs
            ]
        return self._indirect_inputs_with_duplicates

    def indirect_inputs_with_duplicates_with_same_version(self) -> List[NixFlakeInput]:
        """
        Retrieves the list of indirect inputs with duplicates, sharing the same version.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._indirect_inputs_with_duplicates_with_same_version is None:
            indirect_inputs_with_duplicates = self.indirect_inputs_with_duplicates()
            self._indirect_inputs_with_duplicates_with_same_version = [
                input
                for input in indirect_inputs_with_duplicates
                if self.has_duplicates_with_same_version(input)
            ]
        return self._indirect_inputs_with_duplicates_with_same_version

    def indirect_inputs_with_duplicates_with_different_versions(
        self,
    ) -> List[NixFlakeInput]:
        """
        Retrieves the list of indirect inputs with duplicates, with different versions.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._indirect_inputs_with_duplicates_with_different_versions is None:
            indirect_inputs_with_duplicates = self.indirect_inputs_with_duplicates()
            self._indirect_inputs_with_duplicates_with_different_versions = [
                input
                for input in indirect_inputs_with_duplicates
                if self.has_duplicates_with_different_versions(input)
            ]
        return self._indirect_inputs_with_duplicates_with_different_versions

    def all_inputs(self) -> List[NixFlakeInput]:
        """
        Retrieves all inputs.
        :return: Such list.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        if self._all_inputs is None:
            self._all_inputs = []
            [
                self._all_inputs.append(item)
                for item in (self.inputs() + self.indirect_inputs())
                if item is not None and item not in self._all_inputs
            ]
        return self._all_inputs

    def get_duplicates(self, input: NixFlakeInput) -> List[NixFlakeInput]:
        """
        Retrieves the duplicates of given input.
        :param input: The input.
        :type input: pythoneda.shared.nix_flake.NixFlakeInput
        :return: The list of duplicates.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        result = []
        if input is not None:
            for candidate in self.all_inputs():
                if (
                    input != candidate
                    and candidate is not None
                    and input.normalized_name == candidate.normalized_name
                ):
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

    def has_duplicates_with_same_version(self, input: NixFlakeInput) -> bool:
        """
        Checks if given input has duplicates with same version.
        :param input: The input.
        :type input: pythoneda.shared.nix_flake.NixFlakeInput
        :return: True in such case.
        :rtype: bool
        """
        return self.has_duplicates(
            input
        ) and not self.has_duplicates_with_different_versions(input)

    def has_duplicates_with_different_versions(self, input: NixFlakeInput) -> bool:
        """
        Checks if given input has duplicates with different versions.
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

    def all_relationships(self) -> List[NixFlakeInputRelationship]:
        """
        Retrieves all relationships.
        :return: A list with all relationships.
        """
        if self._all_relationships is None:
            self._all_relationships = []
            for source in self.all_inputs():
                for destination in source.inputs:
                    self._all_relationships.append(
                        NixFlakeInputRelationship(source, destination)
                    )
        return self._all_relationships

    def relationships_for_duplicated_nodes(self) -> List[NixFlakeInputRelationship]:
        """
        Retrieves all relationships.
        :return: A list with all relationships.
        """
        if self._relationships_for_duplicated_nodes is None:
            relationships = {}
            self._relationships_for_duplicated_nodes = []
            for source in self.all_inputs():
                for destination in self.get_duplicates(source):
                    if relationships.get(destination, None) is None:
                        self._relationships_for_duplicated_nodes.append(
                            NixFlakeInputRelationship(source, destination)
                        )
                    relationships[source] = destination
        return self._relationships_for_duplicated_nodes
