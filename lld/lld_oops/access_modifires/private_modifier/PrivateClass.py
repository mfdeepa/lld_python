
class PrivateClass():
    __name = "diya"
    age = 35
    def __init__(self):
        self.__name = "diya"

    def __private_method(self):
        print("this is a private method of private super class")
        return f"private attribute name is {self.__name}"

    def name_method(self):
        return self.__name



if __name__ == "__main__":
    a = PrivateClass()
    print(a.age)
   # print(a.name)  we can not access this directly
    print(a.name_method())
    #print(a.private_method) # can not access this directly
