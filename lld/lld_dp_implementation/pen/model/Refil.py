import dataclasses
from ..model.Nib import Nib
from ..model.Ink import Ink
@dataclasses
class Refil:
    __nib: Nib
    __ink:Ink

    def __init__(self, nib: Nib, ink: Ink):
        self.__nib = nib
        self.__ink = ink

    @property
    def ink(self) -> Ink:
        return self.ink
    @ink.setter
    def ink(self, ink: Ink):
        self.ink = ink
