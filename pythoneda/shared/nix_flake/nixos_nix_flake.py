"""
pythoneda/shared/nix_flake/nixos_nix_flake.py

This file defines the NikosNixFlake class.

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

class NixosNixFlake(NixFlake):

    """
    Nix flake for NixOS.

    Class name: NixosNixFlake

    Responsibilities:
        - Packages NixOS's nixpkgs as a Nix flake.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlake
    """

    def __init__(self, version:str):
        """
        Creates a new NixosNixFlake instance.
        :param version: The version.
        :type version: str
        """
        super().__init__(
            "nixos",
            version,
            f"github:NixOS/nixpkgs/nixos-{version}",
            [],
            None,
            "A collection of packages for the Nix package manager",
            "https://github.com/NixOS/nixpkgs",
            "mit",
            list("5000+ contributors"),
            2008,
            "https://nixos.org"
            )
