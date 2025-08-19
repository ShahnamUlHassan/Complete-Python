# Printing simple strings
print('Hello World!')  
print('Shahnam is my name!')

# Printing numbers as strings
print('23')

# DMAS rule (Division, Multiplication, Addition, Subtraction)
print(35 + 35)   # Addition
print(35 - 30)   # Subtraction
print(30 / 5)    # Division
print(30 * 5)    # Multiplication

# Variables and assignment
# "=" is used for assigning a value to a variable
name = 'Shahnam'
age = 27
print('My name is :', name)
print('My age is :', age)

# Data types in Python
# string, int, float, boolean, NoneType
name1 = 'Shahnam'   # String
age1 = 27           # Integer
print(type(name1))  # Output: <class 'str'>
print(type(age1))   # Output: <class 'int'>

age2 = 27
old = False         # Boolean value
a = None            # NoneType
print(type(age2))
print(type(old))
print(type(a))

# Arithmetic operations with two numbers
a = 2
b = 5
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division (float)

# Arithmetic operators
aa = 5
bb = 2
sum1 = aa + bb
print(sum1)        # Output: 7
print(a % b)       # Modulus (remainder)
print(a ** b)      # Exponentiation (a power b)

# Relational / Comparison operators (always return True/False)
c = 50
d = 20
print(c == d)   # Equal to
print(c != d)   # Not equal to
print(c >= d)   # Greater than or equal to
print(c > d)    # Greater than
print(c <= d)   # Less than or equal to
print(c < d)    # Less than

# Assignment operators
num = 10
num = num + 10   # normal addition assignment
num += 10        # shorthand addition assignment
num *= 10        # multiply and assign
num /= 10        # divide and assign
num %= 10        # modulus and assign
num **= 10       # exponentiation and assign
print('num :', num)

# Logical operators (NOT, AND, OR)
e = 50
f = 30
print(not True)        # False
print(not False)       # True
print(not (e > f))     # False, because e > f is True

val1 = True
val2 = True
print('AND operator:', val1 and val2)  # True (both same)

val3 = True
val4 = False
print('OR operator:', val3 or val4)    # True (one value True)
print('OR operator:', (e == f) or (e > f))  # True (because e > f is True)

# Type conversion
cc = 2
dd = 2.45
sum = cc + dd   # int + float = float
print(sum)

ee = 3.14
ee = str(ee)    # converting float to string
print(type(ee))

# Taking input from user
name = input('enter your name:')
print('Welcome', name)

value = input('enter your value')  # by default input is always string
print(type(value), value)

# Multiple inputs
myName = input('enter name: ')
myAge = input('enter age: ')
myMarks = input('enter marks: ')
print('Welcome', myName)
print('age ', myAge)
print('marks', myMarks)

# Practice examples

# Practice 1: Sum of two numbers
first = int(input('enter first: '))
second = int(input('enter second: '))
print('sum =', first + second)

# Practice 2: Area of square
side = float(input('enter square side: '))
print('area =', side * side)

# Practice 3: Average of two numbers
firstNumber = float(input('enter firstNumber: '))
secondNumber = float(input('enter secondNumber: '))
print('avg =', (firstNumber + secondNumber)/2)

# Practice 4: Compare two numbers
number1 = int(input('enter first: '))
number2 = int(input('enter second: '))
print(number1 >= number2)  # will print True if number1 >= number2
