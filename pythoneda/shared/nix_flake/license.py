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
from pythoneda import attribute, primary_key_attribute, Entity

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
    def __init__(self, preamble:str):
        """
        Creates a new license instance.
        :param preamble: The license preamble.
        :type preamble: str
        """
        super().__init__()
        self._preamble = preamble

    @property
    @attribute
    def preamble(self) -> str:
        """
        Retrieves the preamble of the license.
        :return: Such text.
        :rtype: str
        """
        return self._preamble

    @classmethod
    @abc.abstractmethod
    def id(self) -> str:
        """
        Retrieves the id of the license.
        :return: Such id.
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
        return self.__class__.id()

    @classmethod
    def from_id(cls, id:str, copyrightYear:int, copyrightHolder:str, url:str):
        """
        Retrieves the license for given id, customized for given copyright information.
        :param id: The license id.
        :type id: str
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
            if license_class.id() == id:
                result = license_class(copyrightYear, copyrightHolder, url)
                break
        return result
