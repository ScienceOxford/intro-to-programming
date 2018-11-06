from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

with open('light_reading.txt', 'w') as my_file:
    
    my_file.write('Start of light recording\n')
    
    while button_a.was_pressed() is False:
        current_time = int((running_time())/1000)   # time since program started in s
        light = display.read_light_level()
        my_file.write('time = ' + str(current_time) + ', reading = ' + str(light) + '\n')
        sleep(1000)
        
    display.show(Image.GIRAFFE)

with open('light_reading.txt') as my_file:
    content = my_file.read()
    
print(content)
