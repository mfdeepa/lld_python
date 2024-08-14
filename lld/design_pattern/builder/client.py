from lld.design_pattern.builder.Director import ComputerDirector
from lld.design_pattern.builder.GamingComputer import GamingComputerBuilder

if __name__ == '__main__':
    gb = GamingComputerBuilder()
    director = ComputerDirector(gb)
    director.construct()
    c = director.get_computer()
    print(c)