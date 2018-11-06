from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

display.scroll('Hello World')
display.show(Image.HAPPY)
print('program starting...')

while True:
    if button_a.was_pressed() and accelerometer.was_gesture('up'):
        display.show(Image.YES)
        pin1.write_digital(1)
    elif button_b.is_pressed():
        display.show(Image.NO)
    else:
        display.clear()
        print('no button pressed')
    sleep(100)
    pin1.write_digital(0)
