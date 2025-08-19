# ------------------- Lists -------------------
marks = [98, 87, 78, 89, 50]  # list of marks
print(marks)                  # print the list
print(type(marks))            # check the type of 'marks' (list)
print(len(marks))             # print total number of elements in list
print(marks[0])               # print first element
print(marks[1])               # print second element

# Example of list with mixed datatypes
student = ['shahnam', 98, 'lahore']
print(student)
student[0] = 'moon'           # updating first element of list
print(student)

# Slicing a list (index 1 to 3 → elements at position 1,2,3)
marksli = [98, 89, 87, 78, 76, 67]
print(marksli[1:4])

# ------------------- List Methods -------------------

# Append → add element at end of list
list = [2, 1, 3]
list.append(4)
print(list)

# Sort a list in ascending order
sortList = [2, 1, 4, 3]
print(sortList.sort())   # sort() returns None
print(sortList)          # but list is sorted in-place

# Sort in descending order
reversed = [2, 1, 4, 3]
print(reversed.append(5))     # append() also returns None
print(reversed.sort(reverse=True)) # sort in descending order
print(reversed)

# Insert element at specific index
listInserted = [2, 1, 3]
listInserted.insert(1, 5)     # insert 5 at index 1
print(listInserted)

# Remove element by index using pop()
removed = [2, 1, 3, 1]
removed.pop(2)                # removes element at index 2
print(removed)

# ------------------- Tuples -------------------
tup = (2, 1, 3, 1)            # tuple is immutable
print(type(tup))              # check type (tuple)
print(tup[0])                 # print element at index 0
print(tup[1])                 # print element at index 1

# Find index of element in tuple
element = (1, 2, 3, 4)
print(element.index(2))       # returns index of first occurrence of 2

# Count occurrences of an element in tuple
tupCount = (1, 2, 3, 4)
print(tupCount.count(2))      # count how many times 2 appears

# ------------------- Practice 1 -------------------
# Add 3 movies entered by user into a list
movies = []
mov1 = input('enter 1st movie: ')
mov2 = input('enter 2nd movie: ')
mov3 = input('enter 3rd movie: ')

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# ------------------- Practice 2 -------------------
# Palindrome check (same forwards & backwards)
list1 = ['m', 'a', 'a', 'm']
copy_list1 = list1.copy()     # make a copy of list
copy_list1.reverse()          # reverse the copied list

if(copy_list1 == list1):      # check if reversed list == original
    print('palindrome')
else:
    print('not palindrome')    

# ------------------- Practice 3 -------------------
# Count number of 'A' in grade list
grade = ['A', 'D', 'A', 'B', 'C']
print(grade.count('A'))

# ------------------- Practice 4 -------------------
# Sort grades (but you accidentally sorted 'grade' instead of 'grade1')
grade1 = ['D', 'A', 'B', 'D', 'A']
grade1.sort()
print(grade1)
