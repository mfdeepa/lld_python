from abc import ABC, abstractmethod

from lld.lld_oops.abstraction.Animal import Animal


class Dog(Animal):
    def make_sound(self):
        print("dog is barking")
    def move(self):
        print("dog is moving")


def main():
    dog = Dog()
    dog.make_sound()
    dog.move()


