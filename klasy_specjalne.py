class Student:
    school_name = 'ABC'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_school(self, name):
        print(self.school_name)
        self.school_name = name
        print(self.school_name)


tomek = Student('Tomek', 24)
tomek.change_school('XYZ')
print(tomek.school_name)

ania = Student('Ania', 19)
print(ania.school_name)
