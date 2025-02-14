# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/nixpkgs_nix_flake.py

This file defines the NixpkgsNixFlake class.

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


class NixpkgsNixFlake(NixFlake):
    """
    Nix flake for NixOS' nixpkgs.

    Class name: NixpkgsNixFlake

    Responsibilities:
        - Packages NixOS's nixpkgs as a Nix flake.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlake
    """

    def __init__(self, version: str):
        """
        Creates a new NixpkgsNixFlake instance.
        :param version: The version.
        :type version: str
        """
        super().__init__(
            "nixos",
            version,
            "github:NixOS/nixpkgs/{version}",
            [],
            None,
            "A collection of packages for the Nix package manager",
            "https://github.com/NixOS/nixpkgs",
            "mit",
            list("5000+ contributors"),
            2008,
            "https://nixos.org",
        )

    @classmethod
    def default(cls):
        """
        Retrieves the default version of the NixOS/nixpkgs Nix flake input.
        :return: Such instance.
        :rtype: pythoneda.shared.nix.flake.NixpkgsNixFlake
        """
        return cls("24.05")


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
