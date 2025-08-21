# ---------------------------------------
# LOOPS IN PYTHON (CLEAN VERSION)
# ---------------------------------------

# while loop example
count = 1     # loop control variable (iterator)
while count <= 5:   # loop will run until count <= 5
    print('hello')   
    count += 1    # increment by 1
print(count)   # prints 6 after loop ends


# reverse while loop (correct stopping condition)
i = 5
while i >= 1:   # loop runs from 5 down to 1
    print(i)
    i -= 1
print('loop ended')


# practice 1: print numbers 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1


# practice 2: print numbers 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1


# practice 3: print multiplication table of a number
n = int(input('enter your number: '))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


# practice 4: traverse list using while loop
nums = [1, 4, 9, 16, 25, 36, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# practice 5: search element in list
nums = [1, 4, 9, 16, 25, 36, 64, 81, 100]
x = 36
i = 0
while i < len(nums):
    if nums[i] == x:    
        print('found at idx', i)
        break   # stop after finding
    i += 1    


# practice 6: break example
i = 1
while i <= 5:
    print(i)
    if i == 3:   # stop loop when i == 3
        break
    i += 1
print('end of loop')


# break and continue example (print even numbers only)
i = 1
while i <= 10:
    if i % 2 != 0:   # skip odd numbers
        i += 1
        continue
    print(i)   # prints even numbers
    i += 1


# ---------------------------------------
# FOR LOOP EXAMPLES
# ---------------------------------------

# for loop on list
nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val) 


# for loop on tuple
tup = (1, 2, 3, 4, 5)
for num in tup:
    print(num)


# for loop on string (search character)
string = 'Shahnam'
for char in string:
    if char == 'n':
        print('n found')
        break
else:
    print('End')     # runs if loop is not broken


# practice 7: print all elements in list
nums = [1, 2, 3, 4, 5, 6, 7]
for el in nums:
    print(el)


# practice 8: find element in tuple
nums = (1, 2, 3, 4, 0, 9, 8, 7, 6, 5)
x = 9
idx = 0
for el in nums:
    if el == x:
        print('number found at idx', idx)
        break
    idx += 1


# range function examples
for i in range(10):  # range(stop)
    print(i)

for i in range(2, 10):  # range(start, stop)
    print(i)

for i in range(2, 10, 2):  # range(start, stop, step)
    print(i)


# even numbers in range
for i in range(2, 101, 2):   # prints even numbers only
    print(i)


# practice 9: print 1 to 100
for i in range(1, 101):
    print(i)


# practice 10: print 100 to 1
for i in range(100, 0, -1):
    print(i)


# practice 11: multiplication table using for loop
n = int(input('enter a number: '))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# practice 12: pass statement
for i in range(5):
    pass    # placeholder, does nothing
print('some useful work')


# practice 13: sum of n numbers using for loop
n = 7
sum = 0
for i in range(1, n + 1):
    sum += i
print('total sum =', sum)


# practice 14: sum of n numbers using while loop
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print('total sum =', sum)


# practice 15: factorial using while loop
n = 3
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print('factorial =', fact)


# practice 16: factorial using for loop
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print('factorial =', fact)
