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
from .pythoneda_nix_flake import PythonedaNixFlake
from typing import List


class PythonedaSharedPythonedaDomainNixFlake(PythonedaNixFlake):

    """
    Nix flake pythoneda-shared-pythoneda/domain.

    Class name: PythonedaSharedPythonedaDomainNixFlake

    Responsibilities:
        - Provides a way to build pythoneda-shared-pythoneda/domain.
        - Provides a way to run pythoneda-shared-pythoneda/domain.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlake
    """

    def __init__(self, version: str, inputs: List):
        """
        Creates a new PythonedaSharedPythonedaDomainNixFlake instance.
        :param version: The version.
        :type version: str
        :param inputs: The inputs.
        :type inputs: List[pythoneda.shared.nix_flake.NixFlake]
        """
        super().__init__(
            "pythoneda-shared-pythoneda-domain",
            version,
            self.url_for,
            inputs,
            "Support for event-driven architectures in Python",
            "https://github.com/pythoneda-shared-pythoneda/domain",
            "S",
            "D",
            "D",
        )

    def url_for(self, version: str) -> str:
        """
        Retrieves the url for given version.
        :param version: The version.
        :type version: str
        :return: The url.
        :rtype: str
        """
        return f"github:pythoneda-shared-pythoneda/domain-artifact/{version}?dir=domain"
