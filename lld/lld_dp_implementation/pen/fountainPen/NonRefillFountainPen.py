from FountainPen import FountainPen
from ..abstract.NonRefillPen import NonRefillPen
from ..model.Refil import Refil
from ..model.Nib import Nib
from ..model.NibType import NibType
from ..model.InkType import InkType
from ..model.Ink import Ink

class NonRefillFountainPen(FountainPen, NonRefillPen):
    refil:Refil
    def __init__(self,brand, name, type, price, length, writingStrategy, penBody):
        super().__init__(brand, name, type, price, length, writingStrategy, penBody)

    def change_refil(self,refil:Refil):
        ink = Ink("red", 2,InkType.FOUNTAIN)
        nib = Nib(2.5,NibType.FOUNTAIN)
        return refil(ink,nib)