# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/pythoneda_shared_domain_input.py

This file defines the PythonedaSharedDomainInput class.

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
from .nixos_nix_flake import NixosNixFlake
from .pythoneda_nix_flake import PythonedaNixFlake
from .pythoneda_shared_banner_nix_flake import PythonedaSharedBannerNixFlake
from typing import List


class PythonedaSharedDomainNixFlake(PythonedaNixFlake):

    """
    Nix flake pythoneda-shared/domain.

    Class name: PythonedaSharedDomainNixFlake

    Responsibilities:
        - Provides a way to build pythoneda-shared/domain.
        - Provides a way to run pythoneda-shared/domain.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlake
    """

    def __init__(self, version: str):
        """
        Creates a new PythonedaSharedDomainNixFlake instance.
        :param version: The version.
        :type version: str
        """
        super().__init__(
            "pythoneda-shared-domain",
            version,
            self.url_for,
            [
                FlakeUtilsNixFlake("v1.0.0"),
                NixosNixFlake("23.11"),
                PythonedaSharedBannerNixFlake("0.0.47"),
            ],
            "Support for event-driven architectures in Python",
            "https://github.com/pythoneda-shared/domain",
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
        return f"github:pythoneda-shared-def/domain/{version}"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
