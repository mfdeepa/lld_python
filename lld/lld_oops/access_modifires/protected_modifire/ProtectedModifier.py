class ProtectedModifier(object):
    _name = "deepti"

    def __init__(self, name):
        self._name = name

    def student(self):
        return f"this is protected variable name: {self._name}"

    def _value(self):
        print("this is protected variable value")


class ProtectedChild(ProtectedModifier):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print("display:", self._name)

class ABCD:
    def abc_method(self):
    # we can call the protected attribute in other class via class name of protected attribute.
    # we can call the protected method in other class via class name of protected method with self parameter.
        print(ProtectedModifier._name)
        print(ProtectedModifier._value(self))



if __name__ == "__main__":
    obj = ProtectedModifier("deepti")
    print(obj.student())
    print(obj._value())

    obj1 = ProtectedChild("diya")
    print(obj1.student())
    print(obj1._value())  #calling protected method via child class.
    print(obj1.display())

    obj2 = ABCD()
    print(obj2.abc_method())


