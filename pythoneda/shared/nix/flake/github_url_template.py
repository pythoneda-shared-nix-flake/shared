# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/github_url_template.py

This file declares the GithubUrlTemplate class.

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
from pythoneda.shared import primary_key_attribute, ValueObject


class GithubUrlTemplate(ValueObject):
    """
    Defines url_templates for Github-based NixFlakeInputs.

    Class name: GithubUrlTemplate

    Responsibilities:
        - Define an `url_template` for Github inputs.

    Collaborators:
        - None
    """

    def __init__(self, owner: str, repo: str, dir: str = None):
        """
        Creates a new GithubUrlTemplate instance.
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

    def url_template(self) -> str:
        """
        Retrieves the template to get the url for given version.
        :return: The template.
        :rtype: str
        """
        suffix = ""
        if self.dir is not None:
            suffix = f"?dir={self.dir})"

        owner = self.owner
        repo = self.repo
        return f"github:{owner}/{repo}/{{version}}{suffix}"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
