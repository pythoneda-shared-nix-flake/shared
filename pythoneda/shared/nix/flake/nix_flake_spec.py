# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/nix_flake_spec.py

This file declares the NixFlakeSpec class.

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
from pythoneda.shared import attribute, primary_key_attribute, ValueObject
from typing import List


class NixFlakeSpec(ValueObject):
    """
    Specification of a Nix Flake.

    Class name: NixFlakeSpec

    Responsibilities:
        - Defines criteria for a Nix flake.

    Collaborators:
        - pythoneda.ValueObject
    """

    def __init__(self, name: str, versionSpec: str, url: str, inputSpecs: List = []):
        """
        Creates a new NixFlakeSpec instance.
        :param name: The name of the flake.
        :type name: str
        :param versionSpec: The nix flake version specification.
        :type versionSpec: str
        :param url: The url.
        :type url: str
        :param inputSpecs: Specs for the Nix flake's inputs.
        :type inputSpecs: Dict[pythoneda.shared.nix.flake.NixFlakeSpec]
        """
        super().__init__()
        self._name = name
        self._version_spec = versionSpec
        self._url = url
        self._input_specs = [spec for spec in inputSpecs if spec.name != name]

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
    def version_spec(self) -> str:
        """
        Retrieves the version spec.
        :return: Such specification.
        :rtype: str
        """
        return self._version_spec

    @property
    @attribute
    def url(self) -> str:
        """
        Retrieves the url.
        :return: Such url.
        :rtype: str
        """
        return self._url

    @property
    @attribute
    def input_specs(self) -> List:
        """
        Retrieves the specifications for the input's own inputs.
        :return: Such specifications.
        :rtype: List[pythoneda.shared.nix.flake.NixFlakeInputSpec]
        """
        return self._input_specs


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
