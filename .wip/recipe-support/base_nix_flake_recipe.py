"""
pythoneda/shared/nix_flake/recipe/base_nix_flake_recipe.py

This file defines the BaseNixFlakeRecipe class.

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
from .empty_flake_metadata_section_in_recipe_toml import (
    EmptyFlakeMetadataSectionInRecipeToml,
)
from .empty_flake_section_in_recipe_toml import EmptyFlakeSectionInRecipeToml
from .missing_flake_section_in_recipe_toml import MissingFlakeSectionInRecipeToml
from .missing_flake_version_spec_in_recipe_toml import (
    MissingFlakeVersionSpecInRecipeToml,
)
from .missing_recipe_toml import MissingRecipeToml
from .missing_type_in_flake_metadata_section_in_recipe_toml import (
    MissingTypeInFlakeMetadataSectionInRecipeToml,
)
from .more_than_one_flake_in_recipe_toml import MoreThanOneFlakeInRecipeToml
import abc
import inspect
import logging
import os
from pathlib import Path
from pythoneda import Entity, primary_key_attribute
from pythoneda.shared.code_requests.nix_flake import NixFlake
import toml
from typing import Dict, List

class BaseNixFlakeRecipe(Entity, abc.ABC):
    """
    Represents common logic for Nix Flake recipes.

    Class name: BaseNixFlakeRecipe

    Responsibilities:
        - Define a recipe for creating a specific flavor of nix flake.

    Collaborators:
        - None
    """

    _flakes = []

    def __init__(self, flake):
        """
        Creates a new BaseNixFlakeRecipe instance.
        :param flake: The nix flake.
        :type name: pythoneda.shared.nix_flake.NixFlake
        """
        super().__init__()
        self._flake = flake

    @property
    @primary_key_attribute
    def flake(self):
        """
        Retrieves the flake.
        :return: Such instance.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self._flake

    @classmethod
    def initialize(cls):
        """
        Initializes the class, if needed.
        """
        if cls.should_initialize():
            cls._flakes = cls.supported_flakes()
            cls._type = cls.flake_type()

    @classmethod
    def should_initialize(cls) -> bool:
        """
        Checks whether this class needs initialization.
        :return: True in such case.
        :rtype: bool
        """
        return cls != FlakeRecipe

    @classmethod
    def recipe_toml_file(cls) -> str:
        """
        Retrieves the "recipe.toml" file.
        :return: The path of the "recipe.toml" file.
        :rtype: str
        """
        recipe_folder = Path(inspect.getsourcefile(cls)).parent
        return os.path.join(recipe_folder, "recipe.toml")

    @classmethod
    def read_recipe_toml(cls):
        """
        Reads the "recipe.toml" file.
        :return: The contents of the file.
        :rtype: str
        """
        result = ""
        recipe_toml_file = cls.recipe_toml_file()
        if not os.path.exists(recipe_toml_file):
            raise MissingRecipeToml(recipe_toml_file)
        recipe_toml_contents = ""
        with open(recipe_toml_file, "r") as file:
            recipe_toml_contents = file.read()
        result = toml.loads(recipe_toml_contents)
        return result

    @classmethod
    def supported_flakes(cls) -> List[Dict[str, str]]:
        """
        Retrieves the list of supported flakes.
        :return: Such list.
        :rtype: List[Dict[str, str]]
        """
        result = []
        recipe_toml = cls.read_recipe_toml()
        flake_specs = recipe_toml.get("flake", {})
        if not flake_specs:
            raise MissingFlakeSectionInRecipeToml(cls.recipe_toml_file())
        entries = list(flake_specs.keys())
        if not entries or len(entries) == 0:
            raise EmptyFlakeSectionInRecipeToml(cls.recipe_toml_file())
        for flake in entries:
            version_spec = flake_specs.get(flake, "")
            if not version_spec:
                raise MissingFlakeVersionSpecInRecipeToml(flake, cls.recipe_toml_file())
            aux = {}
            aux[flake] = version_spec
            result.append(aux)
        return result

    @classmethod
    def flake_type(cls) -> str:
        """
        Retrieves the type of nix flake.
        :return: Such type.
        :rtype: str
        """
        result = None
        recipe_toml = cls.read_recipe_toml()
        flake_metadata = recipe_toml.get("flake").get("metadata", {})
        if flake_metadata:
            result = flake_metadata.get("type", None)
            if not result:
                raise MissingTypeInFlakeMetadataSectionInRecipeToml(
                    cls.recipe_toml_file()
                )
        return result

    @abc.abstractmethod
    def process(self):  # -> FlakeCreated:
        """
        Performs the recipe tasks.
        """
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def compatible_versions(cls, v1: str, v2: str) -> bool:
        """
        Checks if given versions are compatible.
        """
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def supports(cls, flake) -> bool:
        """
        Checks if this type of recipe supports given flake.
        :param flake: The nix flake.
        :type flake: pythoneda.shared.nix_flake.NixFlake
        """
        raise NotImplementedError()

    @classmethod
    def type_matches(cls, flake) -> bool:
        """
        Checks if this recipe matches the type of given flake.
        :param flake: The nix flake.
        :type flake: pythoneda.shared.nix_flake.NixFlake
        """
        return cls._type == flake.python_package.get_type()

    @classmethod
    def similarity(cls, flake: Flake) -> float:
        """
        Figures out a similarity score between this class and given nix flake.
        :param flake: The nix flake.
        :type flake: pythoneda.shared.nix_flake.NixFlake
        """
        result = 0.0
        partialResults = []
        if cls.supports(flake):
            return 1.0
        if cls.type_matches(flake):
            partialResults.append(0.5)
        for entry in cls._flakes:
            partialResult = 0.0
            name = list(entry.keys())[0]
            version = entry[name]
            if name == flake.name:
                if version == flake.version:
                    return 1.0
                elif cls.compatible_versions(version, flake.version):
                    partialResult = 0.9
                else:
                    partialResult = 0.7
            partialResults.append(partialResult)
        result = max(partialResults)
        logging.getLogger(cls.__name__).debug(
            f"Similarity between recipe {cls.__name__} and flake {flake.name}-{flake.version}: {result}"
        )
        return result

    def usesGitrepoSha256(self) -> bool:
        """
        Whether this recipe uses the sha256 value of the git repository.
        :return: True in such case.
        :rtype: bool
        """
        return False

    def usesPipSha256(self):
        return False

    def remove_duplicates(self, *lists) -> List:
        result = []
        for lst in lists:
            for item in lst:
                if item not in result:
                    result.append(item)
        return result
