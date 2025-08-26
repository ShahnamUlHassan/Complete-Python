# ---------------------------------------
# FUNCTIONS IN PYTHON
# ---------------------------------------

# Example 1: Function with parameters & return
def calc_sum(a, b):   # function definition
    sum_val = a + b   # local variable (avoid using 'sum' as it is a built-in name)
    print(sum_val)    # print result
    return sum_val    # return result

calc_sum(5, 10)   # function call


# Example 2: Function with parameters & return
def calc_cum(a, b):   # parameters a, b
    return a + b      # return sum of a and b

result = calc_cum(1, 2)   # function call with arguments
print(result)             # prints 3


# Example 3: Function without parameters
def print_hello():      # no parameters
    print('hello')      # just prints hello

print_hello()   # call function


# Example 4: Function to calculate average of 3 numbers
def calc_avg(a, b, c):
    sum_val = a + b + c
    avg = sum_val / 3   # average formula
    print(avg)          # print average
    return avg          # return average

calc_avg(1, 2, 3)       # prints 2.0


# ---------------------------------------
# BUILT-IN FUNCTIONS
# ---------------------------------------

# print() → built-in function
print('ShahnamUlHassan', end='$')   # 'end' controls what comes after print instead of newline
print('ShahnamUlHassan')            # default end = '\n'

# len() → gives length of string/list/tuple
print(len("Python"))   # example usage → 6

# type() → gives data type of variable
print(type(10))       # int
print(type(10.5))     # float
print(type("hello"))  # str

# range() → generates sequence of numbers
for i in range(5):   # numbers from 0 to 4
    print(i)


# ---------------------------------------
# USER DEFINED FUNCTIONS
# ---------------------------------------

# Example: Function with default parameters
def calc_prod(a=2, b=4):   # default values: a=2, b=4
    result = a * b
    print(result)
    return result

calc_prod()        # uses default values → 2 * 4 = 8
calc_prod(3, 5)    # override defaults → 3 * 5 = 15


# ---------------------------------------
# PRACTICE 1
cities = ['lahore', 'karachi', 'faisalabad', 'islamabad']
heroes = ['abbu-bakkar', 'umar', 'usman', 'ali']

def print_len(lst):          # parameter lst can be any list
    print(len(lst))          # print length of list

print_len(cities)   # prints 4
print_len(heroes)   # prints 4


# ---------------------------------------
# PRACTICE 2: Factorial using loop
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i           # multiply with i (FIXED mistake: you wrote 'fact *= 1')
    print(fact)
    return fact

cal_fact(6)   # prints 720


# ---------------------------------------
# PRACTICE 3: Currency converter
def converter(usd_val):
    pkr_val = usd_val * 253.53    # conversion rate
    print(usd_val, 'USD =', pkr_val, 'PKR' )
    return pkr_val

converter(2)   # 2 USD = 507.06 PKR


# ---------------------------------------
# Recursion Examples
# ---------------------------------------

# Example 1: Recursive countdown
def show(n):
    if(n == 0):    # base case → stop recursion
        return
    print(n)       # print current n
    show(n - 1)    # recursive call

show(3)   # prints 3, 2, 1


# Example 2: Factorial using recursion
def fact(n):
    if(n == 1 or n == 0):    # base case
        return 1
    return fact(n-1) * n     # recursive step

print(fact(4))   # prints 24


# ---------------------------------------
# PRACTICE 4: Recursive sum from 1 to n
def calc_sum(n):
    if(n == 0):     # base case
        return 0
    return calc_sum(n-1) + n   # FIXED mistake (you wrote '+1' instead of '+n')

total = calc_sum(5)   # 1+2+3+4+5 = 15
print(total)


# ---------------------------------------
# PRACTICE 5: Print list using recursion
def print_list(lst, idx=0):
    if(idx == len(lst)):    # base case → stop when index = length
        return
    print(lst[idx])         # print current element
    print_list(lst, idx+1)  # recursive call

fruits = ['mango', 'litchi', 'banana', 'apple']   # FIXED spelling 'bnana' → 'banana'
print_list(fruits)
