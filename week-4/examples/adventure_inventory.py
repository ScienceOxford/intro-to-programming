import sys

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def start():
    print("You wake up in a strange place.")
    print("On your left is a desk with a note on it, through the door you can see a street.")
    print("To read the note, type READ.  To exit through the door, type LEAVE")
    while True:
        choice = input(">> ")
        if choice == "READ":
            return read()
        if choice == "LEAVE":
            return leave()
        if choice == "QUIT":
            sys.exit()
        else:
            print("Please choose READ or LEAVE")

def read():
    inventory.append('note')
    print("---\n" + "You gained an item! Inventory = " + str(inventory) + "\n---")
    print("The note says: Come to the Red Wizard and ask for Sarah, she'll know what to do.")
    print("As you read the note, you hear a noise behind you.  You are not alone!")
    print("To ask who is there, type ASK.  To rush and attack, type ATTACK.")
    while True:
        choice = input(">> ")
        if choice == "ASK":
            return ask()
        if choice == "ATTACK":
            return attack()
        if choice == "QUIT":
            sys.exit()
        else:
            print("Please choose ASK or ATTACK")
    
def leave():
    print("You chose LEAVE")

def ask():
    print("You chose ASK")

def attack():
    print("You chose ATTACK")

inventory = []

# The first few lines are instructions to your reader
title = "**Choose Your Own Adventure**"
print("Welcome to " + title)
print("Throughout the story, you choose what happens!")
print("Make your choices by following the prompts, type in CAPITAL LETTERS")
print("To close the book, type QUIT")
print()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
# Now we start your story!
start()
