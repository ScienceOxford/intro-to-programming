from microbit import *
import radio

radio.on()

while True:
    if accelerometer.was_gesture('up'):
        radio.send('     ')
        display.show(Image.SQUARE)
    elif button_a.was_pressed():
        radio.send('dot ')
        display.show(Image('00000:00000:00900:00000:00000'))
    elif button_b.was_pressed():
        radio.send('dash ')
        display.show(Image('00000:00000:09990:00000:00000'))
    else:
        sleep(500)
        display.clear()
