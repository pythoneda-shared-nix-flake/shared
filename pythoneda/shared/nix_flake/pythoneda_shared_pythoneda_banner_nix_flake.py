# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix_flake/pythoneda_shared_pythoneda_banner_nix_flake.py

This file defines the PythonedaSharedPythonedaBannerNixFlake class.

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
from .flake_utils_nix_flake import FlakeUtilsNixFlake
from .nix_flake import NixFlake
from .nixos_nix_flake import NixosNixFlake


class PythonedaSharedPythonedaBannerNixFlake(NixFlake):

    """
    Nix flake for pythoneda-shared-pythoneda/banner.

    Class name: PythonedaSharedPythonedaBannerNixFlake

    Responsibilities:
        - Provides a way to build pythoneda-shared-pythoneda/banner.
        - Provides a way to run pythoneda-shared-pythoneda/banner.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlake
    """

    def __init__(self, version: str):
        """
        Creates a new PythonedaSharedPythonedaBannerNixFlake instance.
        :param version: The version.
        :type version: str
        """
        super().__init__(
            "pythoneda-shared-pythoneda-banner",
            version,
            self.url_for,
            [FlakeUtilsNixFlake.default(), NixosNixFlake.default()],
            "pythoneda",
            "Banner for PythonEDA projects",
            "https://github.com/pythoneda-shared-pythoneda/banner",
            "gpl3",
            ["rydnr <github@acm-sl.org>"],
            2023,
            "rydnr",
        )

    def url_for(self, version: str) -> str:
        """
        Retrieves the url for given version.
        :param version: The version.
        :type version: str
        :return: The url.
        :rtype: str
        """
        return f"github:pythoneda-shared-pythoneda/banner/{version}"

    @classmethod
    def default(cls):
        """
        Retrieves the default version of the pythoneda-shared-pythoneda/banner Nix flake input.
        :return: Such instance.
        :rtype: pythoneda.shared.nix_flake.PythonedaSharedPythonedaBannerNixFlake
        """
        return cls("0.0.13")
