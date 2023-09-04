"""
pythoneda/shared/nix_flake/recipe/more_than_one_flake_section_in_recipe_toml.py

This file defines the MoreThanOneFlakeSectionInRecipeToml class.

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


class MoreThanOneFlakeSectionInRecipeToml(Exception):
    """
    A recipe.toml includes more than one entry in its [flake] section.

    Class name: MoreThanOneFlakeSectionInRecipeToml

    Responsibilities:
        - Represents an error caused by several [flake] sections in a recipe.toml file.

    Collaborators:
        - None
    """

    def __init__(self, message=None, extraInfo=None):
        """
        Creates a new MoreThanOneFlakeSectionInRecipeToml instance.
        :param message: The error message.
        :type message: str
        :param extraInfo: Additional information.
        :type extraInfo: Any
        """
        super().__init__(message)
        self.extra_info = extraInfo
