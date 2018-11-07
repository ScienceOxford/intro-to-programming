from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()

with open('new_data.txt', 'w') as my_file:

    while button_a.was_pressed() is False:
        message = radio.receive()
        if message is not None:
            my_file.write(message)

    display.show(Image.GIRAFFE)

with open('new_data.txt') as my_file:
    content = my_file.read()

print(content)
