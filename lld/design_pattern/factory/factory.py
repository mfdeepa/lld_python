#from knight import Knight
#from archer import Archer
from abc import ABC, abstractmethod

from lld.design_pattern.factory.archer import Archer
from lld.design_pattern.factory.knight import Knight


class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self):
        pass



class KnightFactory:
    def create_player(self):
        return Knight()

class ArcherFactory:

    def create_player(self):
        return Archer()