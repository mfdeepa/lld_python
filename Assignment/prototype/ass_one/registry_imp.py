from typing import Dict
import copy
from .registry import ConfigurationPrototypeRegistry
from .app_config import Configuration, ConfigurationType


class ConfigurationPrototypeRegistryImpl(ConfigurationPrototypeRegistry):

    def __init__(self):
        self.prototypes: Dict[ConfigurationType, Configuration] = {}

    def add_prototype(self, configuration: Configuration) -> None:
        self.prototypes[configuration.type_] = configuration
        # raise NotImplementedError('Not implemented yet.')

    def get_prototype(self, type_: ConfigurationType) -> Configuration:
        if type_ not in self.prototypes:
            #raise ValueError(f"No prototype found for type {type_}")
            raise ValueError(f"No prototype found for type {type_}")

        return self.prototypes[type_]

    def clone(self, type_: ConfigurationType) -> Configuration:
        prototype = self.get_prototype(type_)
        return prototype.clone_object()
