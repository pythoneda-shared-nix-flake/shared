"""
pythoneda/shared/nix_flake/recipe/missing_flake_version_spec_in_recipe_toml.py

This file defines the MissingFlakeVersionSpecInRecipeToml class.

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
class MissingFlakeVersionSpecInRecipeToml(Exception):
    """
    In the recipe.toml, the flake in the [flake] section does not include the version spec.

    Class name: MissingFlakeSectionInRecipeToml

    Responsibilities:
        - Represents an error caused by a [flake] section missing the version spec in the recipe.toml file.

    Collaborators:
        - None
    """

    def __init__(self, message=None, extraInfo=None):
        """
        Creates a new MissingFlakeVersionSpecInRecipeToml instance.
        :param message: The error message.
        :type message: str
        :param extraInfo: Additional information.
        :type extraInfo: Any
        """
        super().__init__(message)
        self.extra_info = extraInfo
