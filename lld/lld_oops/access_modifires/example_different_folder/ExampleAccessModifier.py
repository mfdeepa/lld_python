from lld.lld_oops.access_modifires.protected_modifire.ProtectedModifier import ProtectedModifier
from lld.lld_oops.access_modifires.public_modifier.Example import Example


class ExampleAccessModifier(object):
    def __init__(self):
        pass


class PublicExample(Example):
    def __init__(self):

        #if we create child class of different folder of parent class then we have to give
        # super object, so we have to cal constructor like :
        # super(child class name, self).__init__(attributes)

        #super.__init__(self.name,self.age)
        super(PublicExample, self).__init__(self.name,self.age)


class PrivateExample(Example):
    def __init__(self):
        pass

class ProtectedExample(ProtectedModifier):
    def __init__(self):
        pass

class AB:
    def ab_method(self):
    # we can call the protected attribute in other class in different folder via class name of protected attribute.
    # we can call the protected method in other class in different folder via class name of protected method with self parameter.
        return [(ProtectedModifier._name), (ProtectedModifier._value(self))]

if __name__ == '__main__':
    pe = PublicExample()
    print(pe.name,pe.age)

    pro = ProtectedExample()
    print(pro.student())
    print(pro._value())

    ab = AB()
    print("this is AB class method :", ab.ab_method())
