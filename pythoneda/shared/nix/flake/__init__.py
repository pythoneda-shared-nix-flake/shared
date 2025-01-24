# vim: set fileencoding=utf-8
"""
pythoneda/shared/nix/flake/__init__.py

This file ensures pythoneda.shared.nix.flake is a package.

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import sys

from .github_url_template import GithubUrlTemplate
from .license import License
from .fetch_sha256_failed import FetchSha256Failed
from .flake_lock_update_failed import FlakeLockUpdateFailed
from .nix_flake_input import NixFlakeInput
from .nix_flake import NixFlake
from .pythoneda_nix_flake import PythonedaNixFlake
from .pythoneda_shared_pythonlang_banner_nix_flake import (
    PythonedaSharedPythonlangBannerNixFlake,
)
from .pythoneda_shared_pythonlang_domain_nix_flake import (
    PythonedaSharedPythonlangDomainNixFlake,
)
from .pythoneda_shared_pythonlang_infrastructure_nix_flake import (
    PythonedaSharedPythonlangInfrastructureNixFlake,
)
from .flake_utils_nix_flake import FlakeUtilsNixFlake
from .nix_flake_metadata import NixFlakeMetadata
from .nix_flake_input_relationship import NixFlakeInputRelationship
from .nix_flake_spec import NixFlakeSpec
from .nixpkgs_nix_flake import NixpkgsNixFlake
from .nix_flake_spec_for_execution import NixFlakeSpecForExecution

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
