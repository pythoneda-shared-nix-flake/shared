"""
pythoneda/shared/nix_flake/github_url_for.py

This file declares the GithubUrlFor class.

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
from pythoneda import attribute, primary_key_attribute, ValueObject
from typing import Callable, List


class GithubUrlFor(ValueObject):
    """
    Defines url_for functions for Github-based NixFlakeInputs.

    Class name: GithubUrlFor

    Responsibilities:
        - Define an `url_for` function for Github inputs.

    Collaborators:
        - None
    """

    def __init__(self, owner: str, repo: str, dir: str = None):
        """
        Creates a new GithubUrlFor instance.
        :param owner: The owner or organization.
        :type owner: str
        :param repo: The repository name.
        :type repo: str
        :param dir: The folder within the repository where the flake is located.
        :type dir: str
        """
        super().__init__()
        self._owner = owner
        self._repo = repo
        self._dir = dir

    @property
    @primary_key_attribute
    def owner(self) -> str:
        """
        Retrieves the owner or organization.
        :return: The owner.
        :rtype: str
        """
        return self._owner

    @property
    @primary_key_attribute
    def repo(self) -> str:
        """
        Retrieves the repository name.
        :return: The name.
        :rtype: str
        """
        return self._repo

    @property
    @primary_key_attribute
    def dir(self) -> str:
        """
        Retrieves the folder within the repository where the falke is located.
        :return: The folder.
        :rtype: str
        """
        return self._dir

    def url_for(self, version: str) -> str:
        """
        Retrieves the url for given version.
        :param version: The version.
        :type version: str
        :return: The url.
        :rtype: str
        """
        suffix = ""
        if self.dir is not None:
            suffix = f"?dir={self.dir})"

        owner = self.owner
        repo = self.repo
        return f"github:{owner}/{repo}/{version}{suffix}"
