class Animal:
    def sound(self):
        print("Some sound")

class Mammal(Animal):
    def walk(self):
        print("Walks on land")

class Bird(Animal):
    def fly(self):
        print("Flies in the sky")

class Bat(Mammal, Bird):
    def sleep(self):
        print("Sleeps in a cave")

class Cat(Mammal):
    def rest(self):
        print("Rests in a cave")

if __name__ == "__main__":
    cat = Cat()
    cat.rest()
    cat.sound()
    cat.walk()
