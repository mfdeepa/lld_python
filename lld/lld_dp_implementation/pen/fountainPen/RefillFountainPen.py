from ..fountainPen.FountainPen import FountainPen
from ..abstract.RefillPen import RefillPen
from ..model.Ink import Ink
from ..model.Refil import Refil
from ..model.InkType import InkType


class RefillFountainPen(FountainPen, RefillPen):
    def __init__(self,brand, name, type, price, length, writingStrategy, penBody):
        super().__init__(brand, name, type, price, length, writingStrategy, penBody)

    def can_refill(self):
        return True

    def get_refills(self, ink:Ink):
        if self.can_refill is True:
            ink = Ink("white", 2, InkType.FOUNTAIN)
            return Refil(ink)
        return None