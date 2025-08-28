# ==========================
# OOP in Python (Part 1)
# ==========================

# --------------------------
# Example 1: Class & Object
# --------------------------

class Student:
    # Class attribute
    name = 'Shahnam'

# Object (instance of Student class)
s1 = Student()
print(s1.name)  # Accessing class attribute


# --------------------------
# Example 2: Another Class
# --------------------------

class Car:
    # Class attributes
    color = 'blue'
    brand = 'mercedes'

# Creating object
car1 = Car()
print(car1.color)   # Accessing class attribute
print(car1.brand)


# --------------------------
# Constructor (__init__)
# --------------------------

class Student:
    # Constructor -> initializes object attributes
    def __init__(self, name, marks):
        self.name = name        # Instance attribute
        self.marks = marks
        print('Adding a new student in database..')

# Creating objects
s1 = Student('Shahnam!', 97)
print(s1.name, s1.marks)

s2 = Student('Hassan!', 88)
print(s2.name, s2.marks)


# --------------------------
# Class & Instance Attributes
# --------------------------

class Student:
    college_name = 'abc college'   # Class attribute (shared by all objects)

    def __init__(self, name, marks):
        self.name = name           # Instance attribute (unique to each object)
        self.marks = marks
        print('Adding a new student in database..')

# Objects
s1 = Student('Shahnam!', 97)
print(s1.name, s1.marks)

s2 = Student('Hassan!', 88)
print(s2.name, s2.marks)
print(s2.college_name)          # Access via object
print(Student.college_name)     # Access via class


# --------------------------
# Methods in Class
# --------------------------

class Student:
    college_name = 'abcd college'

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance method
    def welcome(self):
        print('Welcome student,', self.name)

    # Instance method (returns marks)
    def get_marks(self):
        return self.marks

# Object
s1 = Student('moon', 97)
s1.welcome()              # Calling method
print(s1.get_marks())     # Getting marks


# --------------------------
# Practice 1: Average Marks
# --------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance method to calculate average marks
    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print('Hi', self.name, 'your avg score is', total/len(self.marks))

# Object
s1 = Student('john', [99, 98, 97])
s1.get_avg()


# --------------------------
# Static Method Example
# --------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Static method (does not use self, works like a utility function)
    @staticmethod
    def get_avg(name, marks):
        total = 0
        for val in marks:
            total += val
        print('Hi', name, 'your avg score is', total/len(marks))

# Object
s1 = Student('john', [99, 98, 97])

# Calling static method (class name required)
Student.get_avg(s1.name, s1.marks)


# --------------------------
# Abstraction Example
# --------------------------

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    # Start method (user doesn't need to know inner working)
    def start(self):
        self.clutch = True 
        self.acc = True
        print('Car started ..')

# Object
car1 = Car()
car1.start()


# --------------------------
# Encapsulation Example
# --------------------------

class Car:
    def __init__(self):
        # Private attributes (cannot be accessed directly outside class)
        self.__acc = False
        self.__brk = False
        self.__clutch = False

    # Public method to start the car
    def start(self):
        self.__clutch = True 
        self.__acc = True
        print('Car started...')

    # Getter methods (to access private attributes safely)
    def get_acc(self):
        return self.__acc
    
    def get_brk(self):
        return self.__brk

    def get_clutch(self):
        return self.__clutch

    # Setter method (to change private attributes safely)
    def apply_brake(self):
        self.__brk = True
        self.__acc = False
        print("Brake applied, car stopped.")

# Object
car1 = Car()
car1.start()
print("Accelerator:", car1.get_acc())
print("Brake:", car1.get_brk())
print("Clutch:", car1.get_clutch())

# Applying brake
car1.apply_brake()


# --------------------------
# Practice 2: Bank Account
# --------------------------

class Account:
    def __init__(self, bal, acc):
        self.balance = bal       # Instance attribute
        self.account_no = acc    # Instance attribute

    # Method to debit (withdraw) money
    def debit(self, amount):
        self.balance -= amount
        print('Rs.', amount, "was debited")
        print('Total balance:', self.get_balance())

    # Method to credit (deposit) money
    def credit(self, amount):
        self.balance += amount
        print('Rs.', amount, 'was credited')

    # Method to check balance
    def get_balance(self):
        return self.balance

# Object
acc1 = Account(10000, 12345)
acc1.debit(1000)      # Withdraw 1000
acc1.credit(500)      # Deposit 500
acc1.credit(40000)    # Deposit 40000
