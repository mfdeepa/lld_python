# re denotes regular expression
import re
from operator import concat

my_list = [1,2,3,4,5,6]
# for i in my_list:
#     print(i)

iterator = iter(my_list)

print(next(iterator))
print(next(iterator))

# custom iterator

class my_iterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end:
            temp = self.start
            self.start += 1
            return temp
        else:
            raise StopIteration

ite = my_iterator(1, 5)

print(next(ite))

for i in ite:
    print(i)


# GENERATORS.....

def my_generator():
    for i in range(50000000):
        yield i
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print("fibonacci.....")

def fib_generator():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

gen = fib_generator()

for _ in range(10):
    print(next(gen))

#re.sub()