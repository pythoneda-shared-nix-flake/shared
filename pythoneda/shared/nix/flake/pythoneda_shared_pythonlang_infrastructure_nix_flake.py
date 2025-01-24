# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/pythoneda_shared_pythonlang_infrastructure_nix_flake.py

This file defines the PythonedaSharedPythonlangInfrastructureNixFlake class.

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
from .nixpkgs_nix_flake import NixpkgsNixFlake
from .pythoneda_nix_flake import PythonedaNixFlake
from .pythoneda_shared_pythonlang_banner_nix_flake import (
    PythonedaSharedPythonlangBannerNixFlake,
)
from .pythoneda_shared_pythonlang_domain_nix_flake import (
    PythonedaSharedPythonlangDomainNixFlake,
)
from typing import List


class PythonedaSharedPythonlangInfrastructureNixFlake(PythonedaNixFlake):
    """
    Nix flake pythoneda-shared-pythonlang/infrastructure.

    Class name: PythonedaSharedPythonlangInfrastructureNixFlake

    Responsibilities:
        - Provides a way to build pythoneda-shared-pythonlang/infrastructure.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlake
    """

    def __init__(self, version: str):
        """
        Creates a new PythonedaSharedPythonlangInfrastructureNixFlake instance.
        :param version: The version.
        :type version: str
        """
        super().__init__(
            "pythoneda-shared-pythonlang-infrastructure",
            version,
            "github:pythoneda-shared-pythonlang-def/infrastructure/{version}",
            [
                FlakeUtilsNixFlake.default(),
                NixpkgsNixFlake.default(),
                PythonedaSharedPythonlangBannerNixFlake.default(),
                PythonedaSharedPythonlangDomainNixFlake.default(),
            ],
            "Shared library for infrastructure layers",
            "https://github.com/pythoneda-shared-pythonlang/infrastructure",
            "S",
            "D",
            "I",
        )

    @classmethod
    def default(cls) -> "PythonedaSharedPythonlangInfrastructureNixFlake":
        """
        Retrieves the default version of the pythoneda-shared-pythonlang/infrastructure Nix flake.
        :return: Such instance.
        :rtype: pythoneda.shared.nix.flake.PythonedaSharedPythonlangInfrastructureNixFlake
        """
        return cls("0.0.85")


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
