'''
This is a workable, but not very efficient or user-friendly, choose-your-own-adventure story.
Test it and see how it works, then think about how you would improve it.
See LINK TO FILE for some ideas, and links, to get you started.
'''

def start():
    print("You wake up in a strange place.")
    print("On your left is a desk with a note on it, through the door you can see a street.")
    print("To read the note, type READ.  To exit through the door, type EXIT")
    while True:
        choice = input(">> ")
        if choice == "READ":
            return read()
        if choice == "EXIT":
            return exit()
        if choice == "QUIT":
            break
        else:
            print("Please choose READ or EXIT")


def read():
    print("The note says: Come to the Red Wizard and ask for Sarah, she'll know what to do.")
    print("As you read the note, you hear a noise behind you.  You're not alone!")
    print("To ask who is there, type ASK.  To rush and attack, type ATTACK.")
    while True:
        choice = input(">> ")
        if choice == "ASK":
            return ask()
        if choice == "ATTACK":
            return attack()
        if choice == "QUIT":
            break
        else:
            print("Please choose ASK or ATTACK")


def ask():
    print("You chose ASK")

def attack():
    print("You chose ATTACK")


# The first few lines are instructions to your reader
title = "**Choose Your Own Adventure!**"
print("Welcome to " + title)
print("Throughout the story, you choose what happens!")
print("Make your choices by following the prompts, type in CAPITAL LETTERS")
print("To close the book, type QUIT")
print()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
# The below line calls the 'start()' function, which means it follows the steps defined above
start()
