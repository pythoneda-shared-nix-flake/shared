"""
pythoneda/shared/nix_flake/recipe/nix_flake_recipe.py

This file defines the NixFlakeRecipe class.

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
from .nix_flake_recipe import NixFlakeRecipe
import abc
from pythoneda import Repo
from pythoneda.shared.nix_flake.nix_flake import NixFlake
from typing import List

class NixFlakeRecipeRepo(Repo, abc.ABC):
    """
    A subclass of Repo that manages Flake recipes.

    Class name: NixFlakeRecipeRepo

    Responsibilities:
        - A repository of NixFlakeRecipe instances.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new NixFlakeRecipeRepo instance.
        """
        super().__init__(FlakeRecipe)

    @abc.abstractmethod
    def find_recipe_classes_by_flake(self, flake:NixFlake) -> List[NixFlakeRecipe]:
        """
        Retrieves the recipe classes matching given flake, if any.
        :param flake: The nix flake.
        :type name: pythoneda.shared.nix_flake.NixFlake
        """
        raise NotImplementedError(
            "find_by_recipe_classes_by_flake() must be implemented by subclasses"
        )
