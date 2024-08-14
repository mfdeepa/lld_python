import dataclasses
from abc import ABC, abstractmethod
from tokenize import String
from .PenType import *
from .Brand import *
from .PenBody import *
from ..strategy.WritingStrategy import WritingStrategy
from dataclasses import dataclass


@dataclass
class Pen(ABC):
    __brand: Brand
    __name:String
    __penType: PenType
    __price: float
    __length: int
    __writingSttrategy: WritingStrategy
    __penBody: PenBody

    def __init__(self,brand:Brand,name: String,penType:PenType,price:float,length:int,writingStrategy:WritingStrategy ):
        self.brand = brand
        self.name = name
        self.penType = penType
        self.price = price
        self.length = length
        self.writingStrategy = writingStrategy

    @abstractmethod
    def write(self):
        pass

    def __str__(self):
        return f"pen body is {self.penBody} name is {self.name}."


