"""
pythoneda/shared/nix_flake/pythoneda_shared_pythoneda_banner_input.py

This file defines the PythonedaSharedPythonedaBannerInput class.

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
from pythoneda.shared.nix_flake import FlakeUtilsInput, NixFlakeInput, Nixos2305Input

class PythonedaSharedPythonedaBannerInput(NixFlakeInput):

    """
    Represents the input for pythoneda-shared-pythoneda/banner.

    Class name: PythonedaSharedPythonedaBannerInput

    Responsibilities:
        - Represents the information about pythoneda-shared-pythoneda/banner flake.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new PythonedaSharedPythonedaBannerInput instance.
        """
        super().__init__(
            "pythoneda-shared-pythoneda-banner",
            "github:pythoneda-shared-pythoneda/banner/0.0.1a16",
            [ Nixos2305Input(), FlakeUtilsInput() ])
