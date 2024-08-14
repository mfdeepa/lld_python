import dataclasses
from ..model.NibType import NibType
@dataclasses
class Nib:
    radius:float
    nib_type:NibType
    def __init__(self,radius,nib_type):
        self.radius=radius
        self.nib_type=nib_type
