"""
pythoneda/shared/nix_flake/flake_utils_nix_flake.py

This file defines the FlakeUtilsNixFlake class.

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
from .nix_flake import NixFlake

class FlakeUtilsNixFlake(NixFlake):

    """
    Represents a flake-utils Nix flake.

    Class name: FlakeUtilsNixFlake

    Responsibilities:
        - Provides a way to build numtide/flake-utils.
        - Provides a way to run numtide/flake-utils.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlake
    """

    def __init__(self, version:str):
        """
        Creates a new FlakeUtilsNixFlake instance.
        :param version: The version.
        :type version: str
        """
        super().__init__(
            "flake-utils",
            version,
            f"github:numtide/flake-utils/{version}",
            [],
            None,
            "Pure Nix flake utility functions",
            "https://github.com/numtide/flake-utils",
            "mit",
            list("https://github.com/zimbatm"),
            2022,
            "https://github.com/numtide"
            )
