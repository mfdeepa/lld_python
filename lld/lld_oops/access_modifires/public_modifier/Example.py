class Example():
    name = "diya"
    age = 35
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def access_public_method(self):
        return f"name is {self.name} and age is {self.age}"



if __name__ == "__main__":
    example = Example("diya", 35)
    print(example.access_public_method())
    print(example.age)
