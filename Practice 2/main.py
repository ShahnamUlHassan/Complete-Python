# -----------------------------
# STRING BASICS
# -----------------------------

# Escape sequence characters
# \n = newline, \t = tab space
str_with_newline = "this is a string.\nwe are creating it in python"
str_with_tab = "this is a string.\twe are creating it in python"

print(str_with_newline)   # Prints string with newline
print(str_with_tab)       # Prints string with tab space

# String concatenation (joining)
str1 = 'Shahnam'
str2 = 'moon'
print(str1 + str2)   # Joins two strings

# Length of a string
str4 = 'Hello!'
print(len(str4))     # Prints number of characters in string

# String indexing (accessing single character by position)
str3 = 'Shahnam'
print(str3[4])       # Prints 5th character (indexing starts from 0)

# String slicing (extracting part of string)
slice = 'shahnam'
print(slice[1:5])    # Prints characters from index 1 to 4

# Negative index slicing
negSlice = "apple"
print(negSlice[-3:-1])  # Prints "pl" (3rd last to 2nd last)

# -----------------------------
# STRING FUNCTIONS
# -----------------------------

# endswith() → checks if string ends with given substring
ends = 'ShahnamUlHassan'
print(ends.endswith('san'))   # True

# capitalize() → converts first character to uppercase
cap = 'shahnam'
print(cap.capitalize())       # Output: "Shahnam"

# replace() → replaces characters
rep = 'helo'
print(rep.replace('o', 'p'))  # Output: "help"

# find() → returns first index of substring
find = 'hello !'
print(find.find('l'))         # Output: 2

# count() → counts occurrences of substring
count = 'hello world'
print(count.count('lo'))      # Output: 1

# -----------------------------
# PRACTICE QUESTIONS
# -----------------------------

# Practice 1 → Find length of name
name = input('enter your name: ')
print('length of your name is : ', len(name))

# Practice 2 → Count $ symbols in string
prac = 'Hi $ im $ symbol '
print(prac.count('$'))        # Output: 2

# -----------------------------
# CONDITIONAL STATEMENTS
# -----------------------------

# Traffic light system
light = 'green'

if(light == 'red'):
    print('stop')
elif(light == 'green'):
    print('go')
elif(light == 'yellow'):
    print('look')
else:
    print('light is broken')

# -----------------------------
# NESTED CONDITIONALS
# -----------------------------

# Check driving eligibility
age = 34
if age >= 18:          # Adult
    if age >= 80:      # Too old
        print('cannot drive')
    else:
        print('can drive')
else:                  # Underage
    print('cannot drive')

# -----------------------------
# PRACTICE PROBLEMS
# -----------------------------

# Practice 3 → Even or Odd
number = int(input('enter a number: '))
reminder = number % 2
if(reminder == 0):
    print('EVEN')
else:
    print('ODD')

# Practice 4 → Largest of three numbers
a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = int(input('enter third number: '))

if a >= b and a >= c:
    print('first number is largest', a)
elif b >= c:
    print('second number is largest', b)
else:
    print('third number is largest', c)

# Practice 5 → Multiple of 5
x = int(input('enter number: '))
if(x % 5 == 0):
    print('multiple of 5')
else:
    print('not a multiple')
