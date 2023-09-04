"""
pythoneda/shared/nix_flake/flake_utils_input.py

This file defines the FlakeUtilsInput class.

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

class FlakeUtilsInput(NixFlakeInput):

    """
    Represents the input for flake-utils.

    Class name: FlakeUtilsInput

    Responsibilities:
        - Represents the information about flake-utils flake.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new FlakeUtilsInput instance.
        """
        super().__init__("flake-utils", "github:numtide/flake-utils/v1.0.0")
