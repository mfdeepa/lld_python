from BallPen import BallPen
from ..abstract.RefillPen import RefillPen
from ..model.Refil import Refil
from ..model.Ink import Ink
from ..model.InkType import InkType

class RefillBallPen(BallPen,RefillPen):
    refil: Refil
    def __init__(self,brand, name, type, price, length, writingStrategy, penBody):
        super().__init__(brand, name, type, price, length, writingStrategy, penBody)

    def can_refill(self):
        return True

    def get_refills(self, ink:Ink):
        if self.can_refill is True:
            inkk = Ink("blue",2,InkType.BALL)
            return self.refil(ink)
        return None