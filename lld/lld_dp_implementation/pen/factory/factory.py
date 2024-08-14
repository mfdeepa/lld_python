#from ..ballPen.BallPen import BallPen
from ..ballPen.BallPen import BallPen
from ..fountainPen.FountainPen import FountainPen
from ..model.PenType import PenType
from ..gelPen.GelPen import GelPen
from ..strategy.DottedWriting import DottedWriting, SmoothWriting
from ..model.PenBody import PenBody


class FactoryPen:
    def __init__(self, pentype:PenType):
        self.pentype = pentype
    # price, writingStrategy,penBody,penType
    if PenType == PenType.GEL:
        pen = GelPen("Cello", "deepa", PenType.GEL, 17.0, 6, DottedWriting(), PenBody.PARTITION_CAP)
    elif PenType == PenType.BALL:
        pen = BallPen("Cello", "deepa", PenType.BALL, 14.0, 5, SmoothWriting(), PenBody.SINGLE_CAP)
    elif PenType == PenType.FOUNTAIN:
        pen = FountainPen("Cross Pen", "Deepali", PenType.FOUNTAIN, 20.0, 6, DottedWriting(), PenBody.PARTITION_CAP)