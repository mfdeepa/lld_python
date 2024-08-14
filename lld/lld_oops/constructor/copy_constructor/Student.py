import copy

class Student:
    name = "deepa"
    age = 35
    roll_no = 101

if __name__ =="__main__":

# shallow copy
    ls = [1,2,3,4]
    shallow_copy = copy.copy(ls)
    #before change
    print("before updating ls value :" , ls)
    print("before updating shallow_copy value :",shallow_copy)
    print()
    #if i change the value of shallow_copy then ls will also change
    #after change the existing value
    ls.append(5)
    shallow_copy.append(20)

    # after change
    print("after updating  ls value :", ls)
    print("after updating shallow_copy value :", shallow_copy)
    print()

    # after change the existing value.

    shallow_copy[2] = 0
    print("after updating  existing ls value :", ls)
    print("after updating existing shallow_copy value :", shallow_copy)
    print()


# Deep copy
    ls1 = [6,7,8,9,10]
    deep_copy = copy.deepcopy(ls1)
    print("before updating ls1 value :", ls1)
    print("before updating deep_value value :", deep_copy)
    print()

    #after change
    ls1.append(13)
    deep_copy.append(12)
    print("after updating ls1 value :", ls1)
    print("after updating deep_value value :", deep_copy)
    print()

    # if we change the existing value then it will not affect the other one.
    ls1[2] = 15
    print("after updating existing ls1 value :", ls1)
    print("after updating existing value of ls1 then deep value :", deep_copy)
    print()