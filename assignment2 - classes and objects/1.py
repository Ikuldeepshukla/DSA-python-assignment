# Define a python class Person with instance object, variables name and age. Set instance object variables in __init__() method. Also define show() method to display name and age.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Name:', self.name)
        print('Age', self.age)

# initialized object 
p1 = Person('Kuldeep', 28)
p2 = Person('Ram', 30)

# using object
p1.show()
p2.show()