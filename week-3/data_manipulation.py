# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
Step 1
Open a .txt file, print the content to see what the data looks like
Split the file at each new line (\n) to get a list of strings
Close the file
'''
my_file = open('light_reading.txt')
content = my_file.read()
#print(content)

lines = content.split("\n")
#print(lines)
my_file.close()

'''
Step 2
Create a new, empty, list
Iterate through each item in the list of strings we created above (lines) and create new lists from the data
[1:-1] means ignore the first and list items
Append each new list to the empty list we created
'''
data = []

for item in lines[1:-1]:
    items = item.split(",")
    #print(items)
    data.append(items)

'''
Step 3
Create a new, empty, dictionary
Iterate through the list we filled above (data)
Split the string to save one the information we want, then convert to integers
Add each pair to the dictionary
'''
dictionary = {}

for element in data:
    #print(element[0])
    #print(element[1])
    key = int(element[0][7:])
    value = int(element[1][11:])
    dictionary[key] = value

print(dictionary)
