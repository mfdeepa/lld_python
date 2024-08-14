from abc import ABC, abstractmethod
from ..model.Ink import Ink

class RefillPen(ABC):
    @abstractmethod
    def can_refill(self):
        pass
    @abstractmethod
    def get_refills(self, ink:Ink):
        pass