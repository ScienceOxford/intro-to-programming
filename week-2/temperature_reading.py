from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

with open('temp_reading.txt', 'w') as my_file:        # open, or create, the temp_reading.txt file, and refer to it as my_file
        
    while button_a.was_pressed() is False:            # while button a has NOT been pressed (i.e. until you press it)
        temp = temperature()                          # check the current temperature, and call it temp
        my_file.write(str(temp))                      # write the current temperature to the text file, after converting it to a string
        my_file.write('\n')                           # so that the next temp reading is on the line below
        sleep(1000)                                   # pause for 1s, before going back to the top of the loop and checking the temperature
        
    display.show(Image.GIRAFFE)                       # after you exit the loop, shows an image

with open('temp_reading.txt') as my_file:            # open the temp_reading.txt file, in read only format
    content = my_file.read()                          # read all the data in the file, and call it content
    
print(content)                                        # print the entire contents of the text file
