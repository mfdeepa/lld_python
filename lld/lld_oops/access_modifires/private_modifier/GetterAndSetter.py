
class GetterAndSetter:
    __university_name = "Delhi University"
    __rollnum = 10

    def __init__(self, course, university_name):
        self.__course = course
        self.__university_name = university_name
        self.__rollnum = 20

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self,course):
        self.__course = course

    def get_university_name(self):
        return self.__university_name

    def set_university_name(self,university_name):
        self.__university_name = university_name

    university_name = property(get_university_name,set_university_name)

    def __private_method_ex(self):
        print("this is a private method")



if __name__ == "__main__":
    obj = GetterAndSetter("Python", "abc")
    print(obj.course)
    obj.course = "Java"
    print(obj.course)

    print(obj.university_name)
    obj.university_name = "scaler academy"
    print(obj.university_name)

    # with the help of name mangling we can print the private method outside the class.
    print(obj._GetterAndSetter__private_method_ex())

