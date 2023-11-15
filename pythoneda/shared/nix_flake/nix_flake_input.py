"""
pythoneda/shared/nix_flake/nix_flake_input.py

This file declares the NixFlakeInput class.

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


class NixFlakeInput(ValueObject):
    """
    An input in a Nix Flake.

    Class name: NixFlakeInput

    Responsibilities:
        - Contains metadata about an input in a Nix Flake.

    Collaborators:
        - pythoneda.ValueObject
    """

    def __init__(
        self, name: str, version: str, urlFor: Callable[[str], str], inputs: List = []
    ):
        """
        Creates a new NixFlakeInput instance.
        :param name: The name of the input.
        :type name: str
        :param version: The version of the input.
        :type version: str
        :param url_for: The function to retrieve the url for a given version.
        :type url_for: Callable[[str], str]
        :param inputs: Its own inputs.
        :type inputs: Dict
        """
        super().__init__()
        self._name = name
        self._version = version
        self._url_for = urlFor
        self._inputs = [input for input in inputs if input.name != name]
        self._follows = []

    @classmethod
    def empty(cls):
        """
        Creates an empty NixFlakeInput instance, required for deserializing from a JSON representation.
        :return: An empty instance.
        :rtype: pythoneda.shared.nix_flake.NixFlakeInput
        """
        return cls(None, None, [])

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name of the input.
        :return: The name.
        :rtype: str
        """
        return self._name

    @property
    @attribute
    def version(self) -> str:
        """
        Retrieves the version of the dependency.
        :return: The version.
        :rtype: str
        """
        return self._version

    @property
    def url_for(self) -> Callable[[str], str]:
        """
        Retrieves a function to obtain the url for a given version.
        :return: Such function.
        :rtype: Callable[[str], str]
        """
        return self._url_for

    @property
    @attribute
    def inputs(self) -> List:
        """
        Retrieves this input's own inputs.
        :return: Such inputs.
        :rtype: List
        """
        return self._inputs

    @property
    def follows(self) -> List:
        """
        Retrieves the list of follows of this input, according to the flake it's bound to.
        :return: The list of other inputs in the flake that are also inputs for this input, and thus can be followed.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        return self._follows

    def bind(self, flake):
        """
        Binds this input to given flake, to take into account the flake's inputs.
        :param flake: The flake.
        :type flake: pythoneda.shared.nix_flake.NixFlake
        """
        self._follows = list(set(self.inputs) & set(flake.inputs))

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == "inputs":
            self._inputs = [NixFlakeInput.from_dict(value) for value in varValue]
        else:
            super()._set_attribute_from_json(varName, varValue)

    def _get_attribute_to_json(self, varName) -> str:
        """
        Retrieves the value of an attribute of this instance, as Json.
        :param varName: The name of the attribute.
        :type varName: str
        :return: The attribute value in json format.
        :rtype: str
        """
        result = None
        if varName == "inputs":
            result = [input.to_dict() for input in self._inputs]
        else:
            result = super()._get_attribute_to_json(varName)
        return result

    @property
    def name_in_camel_case(self) -> str:
        """
        Retrieves the name in camel case.
        :return: The name formatted in camel case.
        :rtype: str
        """
        return self.__class__.kebab_to_camel(self.name)

    def for_version(self, version: str):
        """
        Retrieves a clone of this dependency, with the updated version.
        :param version: The version.
        :type version: str
        :return: A copy of this dependency, updated.
        :rtype: pythoneda.shared.nix_flake.NixFlakeInput
        """
        return self.__class__(self.name, version, self.url_for, self.inputs)
