import sys

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def start():
    print(name + " wakes up in a strange place.")
    print("On their left is a desk with a note on it, ahead they can see a door.")
    print("To read the note, type READ.  To exit through the door, type LEAVE")
    waitForInput()

def read():
    inventory.append('note')
    print("---\n" + name + " gained an item! Inventory = " + str(inventory) + "\n---")
    print("The note says..." + "\n" + "~~~~~~~~~~~~")
    print("Dear " + name + ",")
    print("If you are reading this, our nightmare has come true.")
    print("Come to the Red Wizard and ask for Sarah, she'll know what to do.")
    print("Good luck!")
    print("Weyoun" + "\n" + "~~~~~~~~~~~~")
    print("As " + name + " reads the note, they hear a noise behind them.  They are not alone!")
    print("To ask who is there, type ASK.  To rush and attack, type ATTACK.")
    waitForInput()
    
def leave():
    print(name + " exits the room through the door and steps outside.")
    print("They find themselves on a side street.  To the left is a park.  To the right is a larger, busier, road.")
    print("To head to the park, type PARK.  To head to the road, type ROAD.")
    waitForInput()

def ask():
    print(name + ' calls out loudly, "Who is there? Show yourself!"')
    print('They hear a voice respond, "I am here to help, give me that note!"')
    print("To hand over the note, type GIVE. To turn and make a quick exit, type LEAVE.")
    waitForInput()

def attack():
    global health
    print(name + " rushes towards the source of the noise, ready to fight.")
    print("They can make out a cloaked figure with a staff standing before them.")
    print("Before they can react, the staff sweeps them off their feet!")
    health -= 20
    print("---\n" + name + " is hurt! They have " + str(health) + " health points left!" + "\n---")
    print("To ask who is there, type ASK. To stand up and make a quick exit, type LEAVE.")
    waitForInput()

def park():
    print("You chose PARK")

def road():
    print("You chose ROAD")

def give():
    inventory.remove('note')
    print("---\n" + name + " lost an item! Inventory = " + str(inventory) + "\n---")
    print("The cloaked figure reads the note quietly.")
    print('"It is as I thought..., you must be ' + name + '. Come with me."')
    print("The cloaked figure turns to enter a door behind them. " + name + " can see a dimly lit corridor beyond.")
    print("To follow the figure, type FOLLOW. To ignore them and exit through the other door, type LEAVE.")
    waitForInput()

def follow():
    print("You chose FOLLOW")

# stats and info about your character
health = 100
inventory = []

# the below dictionary contains all allowed choices in the book
choices = {'QUIT': sys.exit,
           'EXIT': sys.exit,
           'READ': read,
           'LEAVE': leave,
           'ASK': ask,
           'ATTACK': attack,
           'PARK': park,
           'ROAD': road,
           'GIVE': give,
           'FOLLOW': follow}

# the below function checks to see if the user's input (ignoring case with .upper()) is in the dictionary
# if it is in the dictionary, it returns the matching value and calls it as a function
def waitForInput():
    while True:
        choice = (input("> ")).upper()
        if choice in choices:
            print("\n")
            return choices[choice]()
        else:
            print("Please choose valid option")
    
# The first few lines are instructions to your reader
title = "**Disappearance at the Red Wizard**"
print("Welcome to " + title)
print("Throughout the story, you choose what happens!")
print("Make your choices by following the prompts.")
print("To close the book, type QUIT or EXIT")
# Now we ask them to choose a name
print("\n" + "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" + "\n")
print("What is your character's name?")
name = (input("> ")).title()
print("\n" + "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" + "\n")
# Now we start your story!
start()
