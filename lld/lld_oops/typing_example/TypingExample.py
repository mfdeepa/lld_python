from typing import Optional,Union, Any, Generic,TypeVar, Type, ClassVar

# 1. incompatible type of assignment(int to string)
a = 10
#a = "Deepa"
print(a)

# 2. float data type but return integer
sqr : float = 0

#def squareDividedByTwo(num : float) -> int: #this will give error of getting float value and return float value while it's expecting integer value.

def squareDividedByTwo(num: float) -> float:
    print(num*num)
    return num//2

sqr = squareDividedByTwo(10.00)

# 3. if we do not want to return anything then we will use None in return type.

def square(num: float) -> None:
    print(num*num)

square(10.00)

# 4. we can define the data type in the square brackets in list,dict,set,
#numbers : list[int] = [1,2,3,4,5, "abc"] # we can not write str data type in the integer data type.
numbers : list[int] = [1,2,3,4,5]
print(numbers)

numdict: dict[int, str] = {1: "abc", 2: "def", 3: "ghi"}
#numdict: dict[int, str] = {1: "abc", 2: "def", "ghi": 3} # this will give error as key should be int and value should be string.

numset : set[int] = {1,2,3,4,5}
#numset : set[int] = {1,2,3,4,5, "hjdsgj"} #represent error as it shoild be int but data conatins string value also.

# 5. 2d array(list of list)
ll : list[list[int]] = [[1,2,3,4,5],[6,7,8,9]]
#ll : list[list[int]] = [[1,2,"jbskj",4,5],[6,7,8,9]] # static typing error of int to sting.

# 6. if we do not want to type 2d list like list[list[int]] gaian and againa and want to use this then we will
#      assign a variable to list[list[int]]

vector = list[list[int]]
ll1 : vector = [[1,2,3,4,5],[6,7,8,9]]

#7. optional parameter : we can import Optional from typing module

def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name}!"

print(greet())

#8. Any keyword accepts all the data type in the val whether it would be string, int, float etc.
def printingMethod(val: Any):
    print(val)
printingMethod(["1"])

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def getPersonName(person: Person) -> str:
    return person.name


getPersonName(Person("John", 20))

# GENERICS...

T = TypeVar("T") # it's a placeholder in which we can write any data type (string, int, float)
            # whatever we have written variable name then we should also write it in the inverted comma.
class Stack(Generic[T]):   # "T" repersent the int, which we passes while calling stack.
    def __init__(self) -> None:
        self.stack: list[T] = []

    def push(self, item: T) -> None:
        self.stack.append(item)

    def pop(self) -> T:
        return self.stack.pop()

stack1 = Stack[int]()

# 8 : If we want to allow only int and float
M = TypeVar('M', int, float)

def add(a1: M, a2: M) -> M:
    return a1 + a2

add(1.0, 1.0)

class A:
    def __init__(self, x: int) -> None:
        self.x = x

class B(A):
    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)

class C(A):
    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)

G = TypeVar('G', bound=A)  # here bound means child class that means all the child class of "A" can use the G placeholder.
#Bound to A and its subclasses

