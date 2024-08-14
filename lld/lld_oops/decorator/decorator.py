
def greet(fx):
    def mgf():
        print("Good Morning")
        fx()
        print("thanks for using the function")
    return mgf

def hello():
    print("Hello")

# with annotation hello() method output will be
@greet
def hello():
    print("Hello World")
print("function is calling with in the annotation", hello())
print()
print(greet(hello)())
print()

# when the function have parameters then we have to give parameter in annotation function.

def pramGreet(fx):
    def mgf(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("thanks for using the function")
    return mgf

@pramGreet
def add(a,b):
    print(a+b)
    return a+b

print(add(1,2))
print()
print(pramGreet(add)(2,3))