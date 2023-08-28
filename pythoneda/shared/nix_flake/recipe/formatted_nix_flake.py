"""
pythoneda/shared/nix_flake/recipe/formatted_nix_flake.py

This file defines the FormattedNixFlake class.

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
from .nix_flake_recipe import NixFlakeRecipe
from pythoneda import Formatting
from pythoneda.shared.nix_flake import License, NixFlake

class FormattedNixFlake(Formatting):
    """
    Augments NixFlake class to include formatting logic required by recipe templates.
    """
    def __init__(self, flk:NixFlake):
        """
        Creates a new FormattedNixFlake instance.
        :param flake: The nix flake.
        :type name: pythoneda.shared.nix_flake.NixFlake
        """
        super().__init__(flk)

    @property
    def flake(self) -> NixFlake:
        """
        Retrieves the NixFlake.
        :return: Such instance.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self._fmt

    def version_with_underscores(self) -> str:
        """
        Retrieves the nix flake version, with underscores.
        :return: Such text.
        :rtype: str
        """
        return self.flake.version.replace(".", "_")

    def description(self) -> str:
        """
        Retrieves the description of the Nix Flake.
        :return: Such text.
        :rtype: str
        """
        return self.flake.description

    def license(self) -> str:
        """
        Retrieves the license of the Nix Flake.
        :return: Such text.
        :rtype: str
        """
        return self.flake.license

    def sha256(self) -> str:
        """
        Retrieves the sha256 hash of the Nix Flake.
        :return: Such value.
        :rtype: str
        """
        return self.flake.sha256

    def repo_url(self) -> str:
        """
        Retrieves the repository url of the Nix Flake.
        :return: Such url.
        :rtype: str
        """
        return self.flake.repo_url

    def repo_rev(self) -> str:
        """
        Retrieves the repository revision of the Nix Flake.
        :return: Such revision.
        :rtype: str
        """
        return self.flake.repo_rev

    def repo_owner(self) -> str:
        """
        Retrieves the repository owner of the Nix Flake.
        :return: Such information.
        :rtype: str
        """
        return self.flake.repo_owner

    def repo_name(self) -> str:
        """
        Retrieves the repository name of the Nix Flake.
        :return: Such information.
        :rtype: str
        """
        return self.flake.repo_name
