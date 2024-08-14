class ClassKeyword:
    name = "deepa"
    roll_number = 1

    @classmethod  #annotation is neccessary to create the method.
    def class_method(cls):
        print("this is a class method. which is different from the static keyword.")
        cls.roll_number += 3
        return f"class method updated value of roll number {cls.roll_number}"

if __name__ == "__main__":
    ClassKeyword.class_method()
    print(ClassKeyword.name)
    print(ClassKeyword.roll_number)
