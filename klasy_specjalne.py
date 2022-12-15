class Student:
    school_name = 'ABC'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):
        print(Student.school_name)
        Student.school_name = name
        print(Student.school_name)


class Teacher(Student):
    @classmethod
    def change_school(cls, name):
        print("2", Teacher.school_name)
        Student.school_name = name
        print("2", Teacher.school_name)


tomek = Student('Tomek', 24)
Student.change_school('XYZ2')
print(tomek.school_name)

ania = Student('Ania', 19)
print(ania.school_name)

stefan = Teacher("Stefan", 45)
Teacher.change_school('XYZ3')
print(stefan.school_name)
