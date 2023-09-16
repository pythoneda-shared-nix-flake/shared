"""
pythoneda/shared/nix_flake/licenses/gpl3.py

This file defines the GPL3 class.

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
from pythoneda.shared.nix_flake import License


class Gpl3(License):

    """
    Represents the GPL license, version 3 or later.

    Class name: Gpl3

    Responsibilities:
        - Provide information about the GPLv3 license.

    Collaborators:
        - None
    """

    def __init__(self, copyrightYear: int, copyrightHolder: str, url: str):
        """
        Creates a new Gpl3 instance.
        :param copyrightYear: The copyright year.
        :type copyrightYear: int
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        :param url: The project url.
        :type url: str
        """
        super().__init__(
            f""" GNU GENERAL PUBLIC LICENSE
 Version 3, 29 June 2007

 Copyright (C) {copyrightYear} {copyrightHolder} {url}

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
""",
                         copyrightYear,
                         copyrightHolder,
                         url)

    @classmethod
    def empty(cls):
        """
        Retrieves an empty instance, required JSON deserialization.
        :return: An empty License instance.
        :rtype: pythoneda.shared.nix_flake.licenses.Gpl3
        """
        return cls(None, None, None)

    @classmethod
    def license_type(self) -> str:
        """
        Retrieves the type of the license.
        :return: Such type.
        :rtype: str
        """
        return "gpl3"
