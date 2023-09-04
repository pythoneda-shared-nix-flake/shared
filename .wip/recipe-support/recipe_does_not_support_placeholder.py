"""
pythoneda/shared/nix_flake/recipe/recipe_does_not_support_placeholder.py

This file defines the RecipeDoesNotSupportPlaceholder class.

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
class RecipeDoesNotSupportPlaceholder(Exception):
    """
    A recipe does not support a required placeholder.

    Class name: RecipeDoesNotSupportPlaceholder

    Responsibilities:
        - Represents an error caused by a template using a placeholder the recipe does not support.

    Collaborators:
        - None
    """

    def __init__(self, message=None, extraInfo=None):
        """
        Creates a new RecipeDoesNotSupportPlaceholder instance.
        :param message: The error message.
        :type message: str
        :param extraInfo: Additional information.
        :type extraInfo: Any
        """
        super().__init__(message)
        self.extra_info = extraInfo
