# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/fetch_sha256_failed.py

This file defines the FetchSha256Failed class.

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
from pythoneda.shared import BaseObject


class FetchSha256Failed(Exception, BaseObject):
    """
    Running nix-prefetch-git failed.

    Class name: FetchSha256Failed

    Responsibilities:
        - Represent the error when running nix-prefetch-git.

    Collaborators:
        - None
    """

    def __init__(self, url: str, rev: str, message: str):
        """
        Creates a new FetchSha256Failed instance.
        :param url: The repository url.
        :type url: str
        :param rev: The repository revision.
        :type rev: str
        :param message: The error message.
        :type message: str
        """
        super().__init__(
            f'"nix-prefetch-git --quiet --url {url} --rev {rev}" failed: {message}'
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
