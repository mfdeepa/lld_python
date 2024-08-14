#from player import Player
from lld.design_pattern.factory.player import Player


class Archer(Player):

    def attack(self):
        print("attack with Bow")