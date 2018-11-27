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
