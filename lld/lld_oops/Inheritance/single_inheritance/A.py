
class A:
    def m(self):
        print("class A")

class B(A):
    def m(self):
        super(A, self).m()
        print("class B")
        super().m()

if __name__ == "__main__":
    ob = B()
    ob.m()