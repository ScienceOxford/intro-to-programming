from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

with open('hello.txt', 'w') as my_file:
    my_file.write("Hello, World!\n")
    my_file.write("Second line...")
    
with open('hello.txt') as my_file:
    content = my_file.read()

changes = content + "\nnew line!"

with open('hello.txt', 'w') as my_file:
    my_file.write(changes)

with open('hello.txt') as my_file:
    content = my_file.read()
print(content)
'''
my_file = open('testfile.txt','w') 
my_file.write("Hello, World!\n")
my_file.write("Second line...")
my_file.close()

my_file = open('testfile.txt')
content = my_file.read()
print(content)
my_file.close()
'''
