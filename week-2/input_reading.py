from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

with open('inputs.txt', 'w') as my_file:
    
    new_text = ''                                       # create a new variable as an empty string
    while new_text != 'exit':                           # while this new variable *is not equal to* (!=) the word 'exit'
        new_text = input('Please input something...')   # ask for an input (type into the repl)
        my_file.write(new_text + '\n')                  # write whatever was typed into the repl to the text file, then start a new line

    display.show(Image.GIRAFFE)

with open('inputs.txt') as my_file:
    content = my_file.read()

print(content)
