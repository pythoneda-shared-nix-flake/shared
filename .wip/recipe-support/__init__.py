"""
pythoneda/shared/code_requests/nix_flake/recipe/__init__.py

This file ensures pythoneda.shared.code_requests.nix_flake.recipe is a package.

Copyright (C) 2023-today rydnr's pythoneda-shared-code-requests/nix-flake

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

from .empty_flake_metadata_section_in_recipe_toml import EmptyFlakeMetadataSectionInRecipeToml
from .empty_flake_section_in_recipe_toml import EmptyFlakeSectionInRecipeToml
from .missing_flake_section_in_recipe_toml import MissingFlakeSectionInRecipeToml
from .missing_flake_version_spec_in_recipe_toml import MissingFlakeVersionSpecInRecipeToml
from .missing_recipe_toml import MissingRecipeToml
from .missing_type_in_flake_metadata_section_in_recipe_toml import MissingTypeInFlakeMetadataSectionInRecipeToml
from .recipe_does_not_support_placeholder import RecipeDoesNotSupportPlaceholder
from .more_than_one_flake_section_in_recipe_toml import MoreThanOneFlakeSectionInRecipeToml
from .formatted_nix_flake import FormattedNixFlake
from .base_nix_flake_recipe import BaseNixFlakeRecipe
from .nix_flake_recipe import NixFlakeRecipe
from .nix_flake_recipe_repo import NixFlakeRecipeRepo
