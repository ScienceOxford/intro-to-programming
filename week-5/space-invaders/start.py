from microbit import *

# set the starting value of x - 2 is the middle column
x = 2
# set the starting pixel
display.set_pixel(x, 4, 9)

while True:
    # if a is pressed, clear the original pixel,
    # then change the value of x,
    # then set the new pixel to on
    if button_a.was_pressed():
        display.set_pixel(x, 4, 0)
        x -= 1
        display.set_pixel(x, 4, 9)
    # if b is pressed, do the same as the above,
    # but in the opposite direction
    if button_b.was_pressed():
        display.set_pixel(x, 4, 0)
        x += 1
        display.set_pixel(x, 4, 9)

# first step: minimise errors - what happens when you reach the edge of the screen?
# before changing the value of x, check that it is less than or equal to 0,
# or greater than or equal to 4
# if x >= 4:

# next step: shooting
# your cannon is always located at (x, y)
# your laser will start there too, then move to (x, y-1), then keep moving upwards
# remember to clear the pixel before so that moves up the screen

# next step: random aliens
# to use the random functions in python, you must -- import random
# random.randint(0,4) will choose a random integer between 0 and 4
# this can be translated into an x coordinate, or a y coordinate

# what happens when your laser hits an alien?
# how does your program know when your laser hits and alien?
