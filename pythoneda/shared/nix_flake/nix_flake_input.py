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
from typing import List

class NixFlakeInput(ValueObject):
    """
    An input in a Nix Flake.

    Class name: NixFlakeInput

    Responsibilities:
        - Contains metadata about an input in a Nix Flake.

    Collaborators:
        - pythoneda.ValueObject
    """

    def __init__(self, name:str, url:str, inputs:List=[]):
        """
        Creates a new NixFlakeInput instance.
        :param name: The name of the input.
        :type name: str
        :param url: The url of the dependency.
        :type url: str
        :param inputs: Its own inputs.
        :type inputs: Dict
        """
        super().__init__()
        self._name = name
        self._url = url
        self._inputs = [ input for input in inputs if input.name != name ]

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
    def url(self) -> str:
        """
        Retrieves the url of the dependency.
        :return: The url.
        :rtype: str
        """
        return self._url

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

    @property
    def name_in_camel_case(self) -> str:
        """
        Retrieves the name in camel case.
        :return: The name formatted in camel case.
        :rtype: str
        """
        return self.to_camel_case(self.name)

    def to_camel_case(self, txt:str) -> str:
        """
        Retrieves given value in camel case.
        :param txt: The value.
        :type txt: str
        :return: The value formatted in camel case.
        :rtype: str
        """
        words = txt.split("-")
        result = ''.join(word.capitalize() for word in words)
        return result[0].lower() + result[1:]
