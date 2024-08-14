from abc import ABC, abstractmethod

# ABC is Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


    def move(self):
        pass



