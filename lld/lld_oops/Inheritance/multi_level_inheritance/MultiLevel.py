
class A:
    def m(self):
        print("A")
    def am(self):
        print("am")

class B(A):
    def m(self):
        print("B")
    def bm(self):
        print("bm")

class C(B):
    def m(self):
        print("C")
    def cm(self):
        print("cm")

if __name__ == "__main__":
    obj = C()
    obj.bm()
    obj.cm()
    obj.am()