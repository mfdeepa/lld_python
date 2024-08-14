import dataclasses
from tokenize import String
from ..model import InkType


@dataclasses
class Ink:
    __color:String
    __quantity: float
    __type: InkType

    def __int__(self, color:String,quantity:float, type:InkType):
        self.__color = color
        self.__quantity = quantity
        self.__type = type