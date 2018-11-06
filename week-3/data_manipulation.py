from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

with open('light_reading.txt') as my_file:
    content = my_file.read()
    lines = content.split("\n")
    #print(lines)

data = []

for item in lines[1:-1]:
    items = item.split(",")
    data.append(items)

dictionary = {}

for element in data:
    key = int(element[0][7:])
    value = int(element[1][11:])
    dictionary[key] = value

print(dictionary)
