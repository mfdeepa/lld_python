from abc import ABC, abstractmethod

class WritingStrategy(ABC):
    @abstractmethod
    def write(self, writer):
        pass