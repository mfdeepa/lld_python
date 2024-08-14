from lld.design_pattern.factory.archer import Archer
from lld.design_pattern.factory.knight import Knight


class CharacterFactory:
    def create_player(self, player_type):
        if player_type == "Knight":
            return Knight()
        if player_type == "Archer":
            return Archer()