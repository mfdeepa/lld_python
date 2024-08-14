# when the child class have mr than 1 parent class and both parent class is child of single parent class
# that time we will call super class of 1 preference of parent class then another parent class after that it will go the
# both super parent class. means first code will run to D -> B -> C -> A

class A:
    def m(self):
        print("In class A")

class B(A):
    def m(self):
        print("In class B")
        super().m()

class C(A):
    def m(self):
        print("In class C")
        super().m()

class D(B,C):
    def m(self):
        print("In class D")
        super().m()
class F(C):
    def m(self):
        print("In class F")
        #super().m()
class G(F):
    def m(self):
        print("In class G")
        super().m()

class E(B,G):
    def m(self):
        print("In class E")
        super().m()

if __name__ == "__main__":
    obj = D()
    obj.m()
    print()
    obj1 = E()
    obj1.m()
