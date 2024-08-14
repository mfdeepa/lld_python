from BallPen import BallPen
from ..abstract.NonRefillPen import NonRefillPen
from ..model.Refil import Refil
from ..model.Ink import Ink
from ..model.Nib import Nib
from ..model.InkType import InkType
from ..model.NibType import NibType

class NonRefillBallPen(BallPen, NonRefillPen):
    def __init__(self,brand, name, type, price, length, writingStrategy, penBody):
        super().__init__(brand, name, type, price, length, writingStrategy, penBody)

    def change_refil(self, refil:Refil):
        ink = Ink("red", 2.5, InkType.BALL)
        nib = Nib(3, NibType.GOLD)
        return Refil(ink, nib)