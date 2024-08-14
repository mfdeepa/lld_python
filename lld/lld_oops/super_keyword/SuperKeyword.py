class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {name} is created")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        print(f"Mammal {name} is created")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        print(f"Bird {name} is created")

class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)
        print(f"Bat {name} is created")

if __name__ == "__main__":
    bat = Bat("Bruce")
