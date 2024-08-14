from lld.lld_oops.access_modifires.private_modifier.PrivateClass import PrivateClass


class PrivateChildClass(PrivateClass):
    def __init__(self):
        super().__init__()

    def child_method(self):
        print("this is a child method.")
        # we can cal private attribute in child class with the help of name mangling so can access with private class.
        # like : _private class name__private attribute name
        return f"parent name id: {self._PrivateClass__name}"

if __name__ == "__main__":
    obj = PrivateChildClass()
    print(obj.child_method())
    #print(obj.__private_method) # we can not cal private method directly in child class.
    print(obj.name_method())

    #print private method of parent class
    print(obj._PrivateClass__private_method())

