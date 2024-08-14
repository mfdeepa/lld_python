#from ..model.Pen import Pen
from lld.lld_dp_implementation.pen.model.Pen import Pen


class BallPen(Pen):
    def __init__(self,brand, name, type, price, length, writingStrategy, penBody):
        super().__init__(brand, name, type, price, length, writingStrategy, penBody)
