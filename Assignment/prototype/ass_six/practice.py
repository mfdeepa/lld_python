class pp:
    def __init__(self,ab,bc):
        self.ab = ab
        self.bc= bc
class pratice(pp):
    def __init__(self, ab, bc, *args):
        super().__init__(ab,bc)
        self.a = 'a'
        print(self.ab,self.bc,*args)


if __name__ == '__main__':
    p = pratice('c','d', 1, 5)
    print(p)