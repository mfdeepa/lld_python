from ..model.Pen import Pen

class FountainPen(Pen):
    def __init__(self, brand, name, type, price, length, writingStrategy, penBody):
        super().__init__(brand, name, type, price, length, writingStrategy, penBody)

