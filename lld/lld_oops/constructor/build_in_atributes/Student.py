class Student:
    """
    this is for the documentation example to access the __doc__ built in class attributes.
    if we write this comment(documentation ) after the attributes name then __doc__ will return None
    instead of print the documentation.
    """
    name = "deepa"
    id = 101
    age = 35
    
    """
    any comment in this line will not print in the doc function.
    """

    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    def display_details(self):
        return f"display the attributes : {self.name,self.id,self.age}"

if __name__ == "__main__":
    s = Student("John",101,22)
    print(s.__doc__)
    print(s.__dict__)
    print(s.__module__)