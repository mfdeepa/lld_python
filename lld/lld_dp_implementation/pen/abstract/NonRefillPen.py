from abc import ABC, abstractmethod
from ..model.Refil import Refil

class NonRefillPen(ABC):
    @abstractmethod
    def change_refil(self,refil:Refil):
        pass