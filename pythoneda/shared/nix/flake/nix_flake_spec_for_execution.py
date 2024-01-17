# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/nix_flake_spec_for_execution.py

This file declares the NixFlakeSpecForExecution class.

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
from .nix_flake_spec import NixFlakeSpec
from pythoneda.shared import primary_key_attribute


class NixFlakeSpecForExecution(NixFlakeSpec):
    """
    Specification of a Nix Flake used to execute code.

    Class name: NixFlakeSpecForExecution

    Responsibilities:
        - Defines criteria for a Nix flake used to execute code.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlakeSpec
    """

    def __init__(self, spec: NixFlakeSpec):
        """
        Creates a new NixFlakeSpecForExecution instance.
        :param spec: The Nix flake spec.
        :type spec: pythoneda.shared.nix.flake.NixFlakeSpec
        """
        super().__init__(
            f"{spec.name}-for-execution", spec.version_spec, spec.url, spec.input_specs
        )
        self._nix_flake_spec = spec

    @property
    @primary_key_attribute
    def nix_flake_spec(self) -> NixFlakeSpec:
        """
        Retrieves the Nix flake spec.
        :return: Such spec.
        :rtype: pythoneda.shared.nix.flake.NixFlakeSpec
        """
        return self._nix_flake_spec

    def __getattr__(self, name: str):
        """
        Retrieves the value of a specific attribute.
        :param name: The attribute name.
        :type name: str
        :return: The attribute's value.
        :rtype: Any
        """
        return getattr(self._nix_flake_spec, name)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
