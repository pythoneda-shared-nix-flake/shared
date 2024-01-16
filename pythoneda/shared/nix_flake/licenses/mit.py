# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix_flake/licenses/mit.py

This file defines the Mit class.

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


class Mit(License):

    """
    Represents the MIT license

    Class name: Mit

    Responsibilities:
        - Provide information about the ASL 2.0 license.

    Collaborators:
        - None
    """

    def __init__(self, copyrightYear: int, copyrightHolder: str, url: str):
        """
        Creates a new MIT instance.
        :param copyrightYear: The copyright year.
        :type copyrightYear: int
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        :param url: The project url.
        :type url: str
        """
        super().__init__(f""" MIT License

 Copyright (C) {copyrightYear} {copyrightHolder} {url}

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
""",
                         copyrightYear,
                         copyrightHolder,
                         url)

    @classmethod
    def empty(cls):
        """
        Retrieves an empty instance, required JSON deserialization.
        :return: An empty License instance.
        :rtype: pythoneda.shared.nix_flake.licenses.Mit
        """
        return cls(None, None, None)

    @classmethod
    def license_type(self) -> str:
        """
        Retrieves the type of the license.
        :return: Such type.
        :rtype: str
        """
        return "mit"
