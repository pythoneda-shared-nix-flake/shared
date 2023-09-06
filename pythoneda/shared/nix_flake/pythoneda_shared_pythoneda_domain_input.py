"""
pythoneda/shared/nix_flake/pythoneda_shared_pythoneda_domain_input.py

This file defines the PythonedaSharedPythonedaDomainInput class.

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
from pythoneda.shared.nix_flake import FlakeUtilsInput, NixFlakeInput, Nixos2305Input, PythonedaSharedPythonedaBannerInput

class PythonedaSharedPythonedaDomainInput(NixFlakeInput):

    """
    Represents the input for pythoneda-shared-pythoneda/domain.

    Class name: PythonedaSharedPythonedaDomainInput

    Responsibilities:
        - Represents the information about pythoneda-shared-pythoneda/domain flake.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new PythonedaSharedPythonedaDomainInput instance.
        """
        super().__init__(
            "pythoneda-shared-pythoneda-domain",
            "github:pythoneda-shared-pythoneda/domain-artifact/0.0.1a40?dir=domain",
            [Nixos2305Input(), FlakeUtilsInput(), PythonedaSharedPythonedaBannerInput()]
        )
