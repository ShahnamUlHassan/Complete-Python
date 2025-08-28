# oops in python (part2)

# del keyword
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student('Hassan')  
print(s1.name)      
del s1

# private(like) attributes & methods
class Person:
    __name = 'abc'

p1 = Person()
print(p1.__name)   # we get an error

# 2
class Person:
    __name = 'abc'

    def __hello(self):
        print('hello user')

    def welcome(self):
        self.__hello

p1 = Person()
print(p1.welcome())

# inheritance

class Car:
    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def stop():
        print('car stopped ..')

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar('fortuner') 
car2 = ToyotaCar('prius')

print(car1.name)
print(car1.start())

# three types of inheritance
# 1 single inheritance

class Car:
    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def stop():
        print('car stopped ..')

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar('fortuner') 
car2 = ToyotaCar('prius')

print(car1.name)
print(car1.start())


# 2 multi-level inheritance

class Car:
    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def stop():
        print('car stopped ..')

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner('diesel')
car1.start()

# 3 multiple inheritance

class A:
    varA = 'welcome to class A'

class B:
    varB = 'welcome to class B'

# class C dono ko inherit kar rahi hai
class C(A, B):
    varC = 'welcome to class C'        

c1 = C()

print(c1.varC)  # output: welcome to class C
print(c1.varB)  # output: welcome to class B
print(c1.varA)  # output: welcome to class A

# super method

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal __init__ called, name = {self.name}")

    def sound(self):
        print("Animals make sounds")

# Child Class
class Dog(Animal):
    def __init__(self, name, breed):
        # super() se parent class ka __init__ call kiya
        super().__init__(name)
        self.breed = breed
        print(f"Dog __init__ called, breed = {self.breed}")

    def sound(self):
        # parent ka method call
        super().sound()
        print("Dog barks: Woof Woof")

# Object create
dog1 = Dog("Tommy", "German Shepherd")
dog1.sound()


# class method

class Student:
    school_name = "ABC School"   # Class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Class Method to change school name
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to {cls.school_name}")

    # Class Method as alternate constructor
    @classmethod
    def from_string(cls, student_str):
        name, marks = student_str.split("-")
        return cls(name, int(marks))


# Normal object
s1 = Student("Ali", 90)

# Alternate constructor se object
s2 = Student.from_string("Ayesha-95")

print("Before:", Student.school_name)

# Class method call
Student.change_school("XYZ School")

print("After:", Student.school_name)
print(s1.name, s1.marks)
print(s2.name, s2.marks)


# property decorator

class Student:
    def __init__(self, name, marks):
        self._name = name          # private attribute
        self._marks = marks        # private attribute

    # Getter
    @property
    def marks(self):
        return self._marks

    # Setter
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Invalid Marks! Must be between 0 and 100.")
        else:
            self._marks = value

    # Deleter
    @marks.deleter
    def marks(self):
        print("Deleting marks...")
        del self._marks


# Object
s1 = Student("Ali", 85)

print("Initial Marks:", s1.marks)    # getter call

s1.marks = 95                        # setter call
print("Updated Marks:", s1.marks)

s1.marks = 120                       # invalid setter

del s1.marks                         # deleter call



# polymorphism : operator overloading
# operators & dunder function

# ===============================
# POLYMORPHISM IN PYTHON EXAMPLES
# ===============================

# 1️⃣ Method Overriding (Runtime Polymorphism)
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):   # overriding parent method
        return "Woof!"

class Cat(Animal):
    def speak(self):   # overriding parent method
        return "Meow!"

print("1️⃣ Method Overriding Example:")
animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())
print("-" * 40)


# 2️⃣ Operator Overloading (Compile-time Polymorphism jaisa)
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):   # + operator overload
        return self.value + other.value

    def __sub__(self, other):   # - operator overload
        return self.value - other.value

    def __mul__(self, other):   # * operator overload
        return self.value * other.value

print("2️⃣ Operator Overloading Example:")
n1 = Number(10)
n2 = Number(5)
print("Addition:", n1 + n2)   # calls __add__
print("Subtraction:", n1 - n2)  # calls __sub__
print("Multiplication:", n1 * n2)  # calls __mul__
print("-" * 40)


# 3️⃣ Duck Typing (Special type of Polymorphism in Python)
class Sparrow:
    def fly(self):
        return "Sparrow flying"

class Airplane:
    def fly(self):
        return "Airplane flying"

class Whale:
    def swim(self):
        return "Whale swimming"

print("3️⃣ Duck Typing Example:")
for obj in [Sparrow(), Airplane()]:
    # Duck typing: agar 'fly' method hai to chalega
    print(obj.fly())
print("-" * 40)


# 4️⃣ Built-in Polymorphism Functions (len(), + operator on strings & lists, etc.)
print("4️⃣ Built-in Polymorphism Example:")
print("Length of string:", len("Hello"))  # len works on string
print("Length of list:", len([1, 2, 3, 4]))  # len works on list
print("String + String:", "Hello " + "World")  # + works on strings
print("List + List:", [1, 2] + [3, 4])  # + works on lists
print("-" * 40)
