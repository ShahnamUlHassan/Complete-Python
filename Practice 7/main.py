# file i/o in python       i/o = input/output
# types of files 1text files = .txt, .docx, .log etc ,,,, 2binary files = .mp4, .mov, .png, .jpeg etc

# open, read & close file

f = open('read.txt', 'r')
data = f.read()
print(data)
print(type(data))
f.close()

# character       with their                     meaning
# 'r'                               open for reading(default)
# 'w'                               open for writing, truncating the first
# 'x'                               create a new file and open it for writing
# 'a'                               open for writing, appending to the end of the file if it exixts
# 'b'                               binary mode
# 't'                               text mode (default)
# '+'                               open a disk file for updating (reading and writing)

# reading a file

# data = f.read() =  reads entire lines

f = open('read.txt', 'r')
data = f.read(5)   # 5 for how much character we need
print(data)
f.close()

# data = f.readline()  =  reads one line line at a time

f = open('read.txt', 'r')
data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

# writing to a file
f = open('write.txt', 'w')

f.write('i want to learn js')   # after doing this we get a sentece which we write we can see in write.txt file after the excute of code
f.close()

# append text with writing a file

f = open('append.txt', 'a')

f.write('then i want to move on reactjs')  # this code append with which code we write already after the excution of code

f.close()

# combine now read and write with read+.txt file and we can see our code after the excution 

f = open('read+.txt', 'r+')
f.write('abc')
print(f.read())
f.close()

f = open('write+txt', 'w+')
print(f.read())
f.write('abc')
f.close()


f = open('append+.txt', 'a+')
print(f.read())
f.write('abc')
f.close()

# with syntax

with open('demo.txt', 'r') as f:
    data = f.read()
    print(data)


with open('demo.txt', 'w') as f:
    f.write('new data')


# deleting a file
# using os module

import os

os.remove('remove.txt')

# practice 1

with open('practice.txt', 'w') as f:   # this method can create a file automatically 
    f.write('hi everyone\nwe are learning file I/O\n')
    f.write('using java\ni like programming in java')


# practice 2

with open('practice.txt', 'r') as f:
    data = f.read()

new_data = data.replace('java', 'python')
print(new_data) 

with open('practice.txt', 'w') as f:
    f.write(new_data)


# practice 3

word = 'learning'
with open('practice.txt', 'r') as f:
    data = f.find()
    if(data.find(word) != -1):
        print('found')
    else:
        print('not found')


# practice 3

def check_for_word():
    word = 'learning'
    with open('practice.txt', 'r') as f:
        data = f.read()
        if(data.find(word) != -1):
            print('found')
        else:
            print('not found')
check_for_word()


# practice 4

def check_for_line():
    word = 'learning'
    data = True
    line_no = 1
    with open('practice.txt', 'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())


# practice 5

count = 0
with open('practice.txt', 'r') as f:
    data = f.read()

    nums = data.split(',')
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)            