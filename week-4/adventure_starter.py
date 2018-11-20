'''
This is a workable, but not very efficient or user-friendly, choose-your-own-adventure story.
Test it and see how it works, then think about how you would improve it.
See LINK TO FILE for some ideas, and links, to get you started.
'''

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

import sys

def start():
    print("You wake up in a strange place.")
    print("On your left is a desk with a note on it, through the door you can see a street.")
    print("To read the note, type READ. To exit through the door, type LEAVE")
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
    print("The note says: Come to the Red Wizard and ask for Sarah, she'll know what to do.")
    print("As you read the note, you hear a noise behind you.  You are not alone!")
    print("To ask who is there, type ASK. To rush and attack, type ATTACK.")
    while True:
        choice = input(">> ")
        if choice == "ASK":
            return ask()
        if choice == "ATTACK":
            return attack()
        if choice == "QUIT":
            sys.exit()
        else:
            print("Please choose ASK or ATTACK, or you can QUIT")
    
def leave():
    print("After running, screaming, for a few hours you calm down sufficiently")
    print("To return to the 'strange place', type START.")
    while True:
        choice = input(">> ")
        if choice == "START":
            return start()
        if choice == "QUIT":
            sys.exit()
        else:
            print("Please choose START, or you can QUIT")

def ask():
    print("You close your eyes tight and shout who's there?")
    print("You hear the words you have always dreaded 'Deal or No Deal'... Its Edmonds!!")
    print("To exit through the door, type LEAVE. To rush and attack, type ATTACK.")
    while True:
        choice = input(">> ")
        if choice == "LEAVE":
            return leave()
        if choice == "ATTACK":
            return attack()
        if choice == "QUIT":
            sys.exit()
        else:
            print("Please choose LEAVE or ATTACK, or you can QUIT")

def attack():
    print("You spin around to look you're attacker in the eye... Its Edmonds!")
    print("You kick him in the 'Crinkley Bottom' and he scarpers")
    print("The evil Edmonds is no more... You have successfully completed your adventure")
    print("Type QUIT and go and have a cold drink!")
    print("... or type START and take a different path through the adventure")
    while True:
        choice = input(">> ")
        if choice == "START":
            return start()
        if choice == "QUIT":
            sys.exit()
        else:
            print("Please choose QUIT, or you can START your adventure again")

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
