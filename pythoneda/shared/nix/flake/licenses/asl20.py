# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/licenses/asl20.py

This file defines the Asl20 class.

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
from pythoneda.shared.nix.flake import License


class Asl20(License):

    """
    Represents the Apache Software license, 2.0

    Class name: Asl20

    Responsibilities:
        - Provide information about the ASL 2.0 license.

    Collaborators:
        - None
    """

    def __init__(self, copyrightYear: int, copyrightHolder: str, url: str):
        """
        Creates a new Asl20 instance.
        :param copyrightYear: The copyright year.
        :type copyrightYear: int
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        :param url: The project url.
        :type url: str
        """
        super().__init__(
            f""" Apache License 2.0

 Copyright (C) {copyrightYear} {copyrightHolder} {url}

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
""",
            copyrightYear,
            copyrightHolder,
            url,
        )

    @classmethod
    def empty(cls):
        """
        Retrieves an empty instance, required JSON deserialization.
        :return: An empty License instance.
        :rtype: pythoneda.shared.nix.flake.licenses.Asl20
        """
        return cls(None, None, None)

    @classmethod
    def license_type(self) -> str:
        """
        Retrieves the type of the license.
        :return: Such type.
        :rtype: str
        """
        return "asl20"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
