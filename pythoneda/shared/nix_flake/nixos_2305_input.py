"""
pythoneda/shared/nix_flake/nixos_2305_input.py

This file defines the Nikos2305Input class.

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
from pythoneda.shared.nix_flake import NixFlakeInput

class Nixos2305Input(NixFlakeInput):

    """
    Represents the input for Nixos 23.05.

    Class name: Nixos2305Input

    Responsibilities:
        - Represents the information about Nixos 23.05 flake.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Nixos2305Input instance.
        """
        super().__init__("nixos", "github:NixOS/nixpkgs/nixos-23.05")
