from lld.lld_oops.abstraction.Animal import Animal
from lld.lld_oops.abstraction.Dog import Dog
from lld.lld_oops.abstraction.College import College
from lld.lld_oops.access_modifires.private_modifier.PrivateClass import PrivateClass
from lld.lld_oops.access_modifires.protected_modifire.ProtectedModifier import ProtectedModifier


class ProtectedExample(ProtectedModifier):
    def __init__(self):
        pass

class pvt(PrivateClass):
    def __init__(self):
        pass

if __name__ == '__main__':
    dog = Dog()
    dog.make_sound()
    dog.move()

    # animal = Animal()    # we can not create object of abstract method
    # animal.make_sound()
    # animal.move()

    college = College()  # we can create object of this abstract class as we haven't used decorator(@abstractmethod) with method.
    print(college.course())
    college.enrollment_number()

    pt = pvt()
    print(pt._PrivateClass__private_method())


    pro = ProtectedExample()
    print(pro.student())
    print(pro._value())