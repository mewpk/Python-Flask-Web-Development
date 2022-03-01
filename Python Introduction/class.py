age = 16
name = "ploy"
def show():
    print(f"My name is {name} I'm {age} years old")
show()

#class 
class Student:
    age = 10
    name = "Ploy"

    def show(self):
        print(f"My name is {self.name} I'm {self.age} years old")

s1 = Student()
s1.show()


#Attributs
class Person:
    class_attr = 20

    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Patsa",18)
print(p1.name)