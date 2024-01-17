# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/nix_flake_input_relationship.py

This file declares the NixFlakeInputRelationship class.

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
from .nix_flake_input import NixFlakeInput
from pythoneda.shared import primary_key_attribute, ValueObject


class NixFlakeInputRelationship(ValueObject):
    """
    A relationship between Nix Flakes.

    Class name: NixFlakeInputRelationship

    Responsibilities:
        - Represents a relationship between two Nix flakes.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlakeMetadata
        - pythoneda.shared.ValueObject
    """

    def __init__(self, source: NixFlakeInput, destination: NixFlakeInput):
        """
        Creates a new NixFlakeInputRelationship instance.
        :param source: The source input.
        :type source: pythoneda.shared.nix.flake.NixFlakeInput
        :param destination: The destination (meaning the source has this instance as input).
        :type destination: pythoneda.shared.nix.flake.NixFlakeInput
        """
        super().__init__()
        self._source = source
        self._destination = destination

    @property
    @primary_key_attribute
    def source(self) -> NixFlakeInput:
        """
        Retrieves the source of the relationship.
        :return: Such input.
        :rtype: pythoneda.shared.nix.flake.NixFlakeInput
        """
        return self._source

    @property
    @primary_key_attribute
    def destination(self) -> NixFlakeInput:
        """
        Retrieves the destination of the relationship.
        :return: Such input.
        :rtype: pythoneda.shared.nix.flake.NixFlakeInput
        """
        return self._destination


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
