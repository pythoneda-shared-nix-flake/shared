# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix_flake/license.py

This file defines the License class.

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
import abc
from pythoneda.shared import attribute, primary_key_attribute, Entity


class License(Entity, abc.ABC):

    """
    Represents a license in Nix.

    Class name: License

    Responsibilities:
        - Enumerate the different licenses.
        - Provide information about the license.

    Collaborators:
        - None
    """

    def __init__(
        self, preamble: str, copyrightYear: int, copyrightHolder: str, url: str
    ):
        """
        Creates a new license instance.
        :param preamble: The license preamble.
        :type preamble: str
        :param copyrightYear: The copyright year.
        :type copyrightYear: int
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        :param url: The project url.
        :type url: str
        """
        super().__init__()
        self._preamble = preamble
        self._copyright_year = copyrightYear
        self._copyright_holder = copyrightHolder
        self._url = url

    @classmethod
    def empty(cls):
        """
        Retrieves an empty instance, required JSON deserialization.
        :return: An empty License instance.
        :rtype: pythoneda.shared.nix_flake.License
        """
        return cls(None, None, None, None)

    @property
    @attribute
    def preamble(self) -> str:
        """
        Retrieves the preamble of the license.
        :return: Such text.
        :rtype: str
        """
        return self._preamble

    @property
    @attribute
    def copyright_year(self) -> str:
        """
        Retrieves the copyright year of the license.
        :return: Such year.
        :rtype: int
        """
        return self._copyright_year

    @property
    @attribute
    def copyright_holder(self) -> str:
        """
        Retrieves the copyright holder of the license.
        :return: Such name.
        :rtype: str
        """
        return self._copyright_holder

    @property
    @attribute
    def url(self) -> str:
        """
        Retrieves the url of the license.
        :return: Such url.
        :rtype: str
        """
        return self._url

    @classmethod
    @abc.abstractmethod
    def license_type(self) -> str:
        """
        Retrieves the type of the license.
        :return: Such type.
        :rtype: str
        """
        pass

    @property
    def license_id(self) -> str:
        """
        Retrieves the id of the license.
        :return: Such id.
        :rtype: str
        """
        return self.__class__.license_type()

    @classmethod
    def from_id(cls, idValue: str, copyrightYear: int, copyrightHolder: str, url: str):
        """
        Retrieves the license for given id, customized for given copyright information.
        :param idValue: The license id.
        :type idValue: str
        :param copyrightYear: The copyright year.
        :type copyrightYear: int
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        :param url: The project url.
        :type url: str
        :return: The license, of None if none found.
        :rtype: pythoneda.shared.nix_flake.License
        """
        result = None
        for license_class in License.__subclasses__():
            if license_class.license_type() == idValue:
                result = license_class(copyrightYear, copyrightHolder, url)
                break
        return result
