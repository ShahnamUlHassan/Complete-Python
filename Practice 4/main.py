# ---------------------------------
# Dictionary in Python
# ---------------------------------

# Dictionary with different datatypes (string, list, tuple, int, string as bool)
info = {
    'name': 'shahnam',
    'subjects': ['python', 'java', 'c++'],
    'topics': ('dict', 'set'),
    'age': 27,
    'id-adult':'True',
}

print(info)                 # prints the whole dictionary
print(info['name'])         # accessing value using key

# Creating empty dictionary and adding key-value pair later
null_dictionary = {}
null_dictionary['name'] = 'shahnam'
print(null_dictionary)

# Nested dictionary (dictionary inside dictionary)
students = {
    'name': 'shahnam',
    'subjects': {
        'phy': 97,
        'bio': 67,
        'eng': 87
    }
}
print(students)             # prints entire nested dictionary
print(students['subjects']) # prints inner dictionary only

# ---------------------------------
# Dictionary methods
# ---------------------------------

# keys() method -> returns all keys
student = {
    'name': 'shahnam',
    'subject': {
        'phy': 97,
        'bio': 67,
        'eng': 87
    }
}
print(student.keys())

# values() method -> returns all values
student = {
    'name': 'shahnam',
    'subject': {
        'phy': 97,
        'bio': 67,
        'eng': 87
    }
}
print(student.values())

# items() method -> returns key-value pairs in tuple form
student = {
    'name': 'shahnam',
    'subject': {
        'phy': 97,
        'bio': 67,
        'eng': 87
    }
}
print(list(student.items()))

# get() method -> safe way to access value using key
student = {
    'name': 'shahnam',
    'subject': {
        'phy': 97,
        'bio': 67,
        'eng': 87
    }
}
print(student['name'])      # direct access
print(student.get('name'))  # using get()

# update() method -> adds new key-value pair
student = {
    'name': 'shahnam',
    'subject': {
        'phy': 97,
        'bio': 67,
        'eng': 87
    }
}
student.update({'city':'lahore'})
print(student)

# ---------------------------------
# Set in Python
# ---------------------------------

# Creating a set (unique, unordered elements)
collection = {1, 2, 4, 6}
print(collection)
print(len(collection))   # length of set

# Empty set (must use set(), {} creates dict)
a = set()

# add() method -> adds elements to a set
addMethod = set()
addMethod.add(1)
addMethod.add(2)
addMethod.add(3)
print(addMethod)

# remove() method -> removes a specific element
removeMethod = {1, 2}
removeMethod.remove(2)
print(removeMethod)

# clear() method -> removes all elements
collection = {2, 4, 6, 4, 5}  # duplicate 4 ignored
collection.clear()
print(collection)

# pop() method -> removes and returns a random element
collection = {'nextjs', 'reactjs', 'js', 'python'}
print(collection.pop())

# union() method -> combines two sets (unique values only)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))

# intersection() method -> returns common elements in both sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))

# ---------------------------------
# Practice examples
# ---------------------------------

# Practice 1: Dictionary with multiple meanings for same word
dictionary = {
    'cat': 'a small animal',
    'table': ['a piece of furniture', 'list of facts & figures']
}
print(dictionary)

# Practice 2: Set automatically removes duplicates
subjects = {'python', 'java', 'js', 'python', 'c++'}
print(subjects)

# Practice 3: Taking marks input and storing in dictionary
marks = {}
x = int(input('Enter phy: '))
marks.update({'phy': x})
x = int(input('Enter math: '))
marks.update({'math': x})
x = int(input('Enter chem: '))
marks.update({'chem': x})
print(marks)

# Practice 4: Set with float & int values
values = {9, 9.5, 8, 8.5}
print(values)

# Practice 5: Set of tuples (immutable inside set)
values = {
    ('float', 9.5),
    ('int', 9)
}
print(values)
