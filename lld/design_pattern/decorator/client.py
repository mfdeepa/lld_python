from lld.design_pattern.decorator.basePizza import BasePizza
from lld.design_pattern.decorator.paneer import Paneer

if __name__ == "__main__":
    inputt = "Base"
    Addon = "Paneer, Cheese, Mushroom"

    addons = Addon.split(",")

    Pza = BasePizza()
    Panner_pza = Paneer(Pza)

    print(Panner_pza.get_price())