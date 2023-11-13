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
import json
from pythoneda import attribute, Entity
import subprocess
from typing import Dict


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
