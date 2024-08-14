from lld.design_pattern.prototype.Monstor import Monstor
import copy

class Zombie(Monstor):
    def __init__(self, health):
        self.health = health

    def attack(self):
        print("Zombie attacking")

    def clone(self):
        return copy.deepcopy(self)

