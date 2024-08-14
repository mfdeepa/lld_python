
class StaticKeyword:
    @staticmethod
    def add_num(a,b):
        return a+b


if __name__ == '__main__':
    print(StaticKeyword.add_num(1,2))

    obj = StaticKeyword()
    print(obj.add_num(1,2))
    print(StaticKeyword.add_num(5,4))
    print(StaticKeyword().add_num(2,3))