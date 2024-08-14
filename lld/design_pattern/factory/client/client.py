#from factory import KnightFactory
from lld.design_pattern.factory.CharacterFactory import CharacterFactory
from lld.design_pattern.factory.factory import KnightFactory



def create_player(player_val):
    player = CharacterFactory().create_player(player_val)
    player.attack()
    # if player_val == "Knight":
    #     KnightFactory().create_player().attack()

if __name__ == '__main__':
    create_player("knight")