import sys

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def start():
    print("You wake up in a strange place.")
    print("On your left is a desk with a note on it, through the door you can see a street.")
    print("To read the note, type READ.  To exit through the door, type LEAVE")
    waitForInput()

def read():
    print("The note says: Come to the Red Wizard and ask for Sarah, she'll know what to do.")
    print("As you read the note, you hear a noise behind you.  You are not alone!")
    print("To ask who is there, type ASK.  To rush and attack, type ATTACK.")
    waitForInput()
    
def leave():
    print("You chose LEAVE")

def ask():
    print("You chose ASK")

def attack():
    print("You chose ATTACK")

# the below dictionary contains all allowed choices in the book
choices = {'QUIT': sys.exit,
           'EXIT': sys.exit,
           'READ': read,
           'LEAVE': leave,
           'ASK': ask,
           'ATTACK': attack} 

# the below function checks to see if the user's input (ignoring case with .upper()) is in the dictionary
# if it is in the dictionary, it returns the matching value and calls it as a function
def waitForInput():
    while True:
        choice = (input("> ")).upper()
        if choice in choices:
            return choices[choice]()
        else:
            print("Please choose valid option")
    
# The first few lines are instructions to your reader
title = "**Choose Your Own Adventure**"
print("Welcome to " + title)
print("Throughout the story, you choose what happens!")
print("Make your choices by following the prompts.")
print("To close the book, type QUIT or EXIT")
print()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
# Now we start your story!
start()
