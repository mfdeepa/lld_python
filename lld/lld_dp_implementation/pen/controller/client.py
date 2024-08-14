#from lld.lld_dp_implementation.pen.factory.factory import FactoryPen
from lld.lld_dp_implementation.pen.factory.factory import FactoryPen
from lld.lld_dp_implementation.pen.model.PenBody import PenBody
from lld.lld_dp_implementation.pen.model.PenType import PenType
from lld.lld_dp_implementation.pen.strategy.DottedWriting import DottedWriting

if __name__ == '__main__':
    pen = FactoryPen("BALL")
    print(pen)