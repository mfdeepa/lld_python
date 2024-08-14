from functools import reduce


mul = lambda x,y : x*y
print(mul(2,3))

is_even = lambda x: x % 2 == 0

print(is_even(2))
print(is_even(3))

# high order function -> MAP, filter, Reduce

# map function implementation

nums = [1,2,3,4,5]

square = list(map(lambda x: x**2, nums))
print(square)

# filter implementation : it accepts function , return object, filter is behaving like a if condition.

even_filter = list(filter(lambda x: x%2 == 0, nums))
print(even_filter)

# Reduce : reducing the data. it is a sequence of single item. we can use it, where we need single value return.

nums = [1,2,3,4,5]

total = reduce(lambda x,y: x+y, nums)  # here x is behaving like a cumulative sum.

print(total)

# if we pass the initial value then we will write function like
total = reduce(lambda x,y: x+y, nums, 1)
print(total)

# find the max value in the list

max_value = reduce(lambda x,y: max(x,y), nums)
print(max_value)

# concatenating the words
words = ["hello", " ", "world"]

conc = reduce(lambda x,y: x+y , words)
print(conc)

# removing the space

remove_space = reduce(lambda x,y : x+y ,list(filter(lambda word: word != " ", words)))
print(remove_space)

numbers= [1,2,3,2,1,5,1,4,5,9,10,3]
distinct_numbers = (lambda x: list(set(x)))(numbers)
print(distinct_numbers)


def is_even(num):
    return num % 2 == 0


def double(num):
    return num * 2

# TODO: Implement the function below
numbers = [1,2,3,4,5,6,7,8,9]
value = list(filter(lambda x :is_even(x), numbers))
print(value)
double_value = list(map(lambda x: x*2, value))
print(double_value)
    # code here

double_val = list(map(lambda x: double(x) ,list(filter(lambda x: is_even(x),numbers))))
print(double_val)

fruits = ['apple', 'banana', 'avocado', 'orange', 'apricot']
fliter_fruit = list(filter(lambda x: x[0] == 'a' or x[0] == 'A', fruits))
print(fliter_fruit)