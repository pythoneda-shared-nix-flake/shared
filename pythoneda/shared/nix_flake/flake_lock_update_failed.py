"""
pythoneda/shared/nix_flake/nix_flake.py

This file defines the FlakeLockUpdateFailed class.

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


class FlakeLockUpdateFailed(Exception):
    """
    Running nix flake update failed.

    Class name: FlakeLockUpdateFailed

    Responsibilities:
        - Represent the error when running nix flake update.

    Collaborators:
        - None
    """

    def __init__(self, repositoryFolder: str, subfolder: str):
        """
        Creates a new instance.
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
        :param subfolder: The subfolder of the flake.nix file.
        :type subfolder: str
        """
        super().__init__(
            f'"nix flake update {subfolder}" in folder {repositoryFolder} failed'
        )
