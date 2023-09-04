"""
pythoneda/shared/nix_flake/recipe/missing_flake_section_in_recipe_toml.py

This file defines the MissingFlakeSectionInRecipeToml class.

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


class MissingFlakeSectionInRecipeToml(Exception):
    """
    A recipe.toml includes an missing [flake] section.

    Class name: MissingFlakeSectionInRecipeToml

    Responsibilities:
        - Represents an error caused by an missing [flake] section in the recipe.toml file.

    Collaborators:
        - None
    """

    def __init__(self, message=None, extraInfo=None):
        """
        Creates a new MissingFlakeSectionInRecipeToml instance.
        :param message: The error message.
        :type message: str
        :param extraInfo: Additional information.
        :type extraInfo: Any
        """
        super().__init__(message)
        self.extra_info = extraInfo
