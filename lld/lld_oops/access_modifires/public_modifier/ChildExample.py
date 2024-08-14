from lld.lld_oops.access_modifires.public_modifier.Example import Example


class ChildExample(Example):
    def __init__(self):
        super().__init__(self.name,self.age)


if __name__ == '__main__':
    obj = ChildExample()
    print(obj.name)