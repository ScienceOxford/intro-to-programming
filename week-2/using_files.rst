Writing to, and reading from, text files on a BBC micro:bit
-------------

The micro:bit can store files, similarly to how your computer can store files.
We need to ask the micro:bit to open a file, before it can read it, or edit it (like opening a word document on your computer for example).
It also needs to be told whether to open the file as a writable file, or as read-only.


To open a file as writeable, and then put some text in it, you can use the following::

    from microbit import *
    with open('hello.txt', 'w') as my_file:
        my_file.write("Hello, World!\n")
        my_file.write("Second line...")


If you click the ‘files’ button on the Mu taskbar, you should now see hello.txt listed as a file.
Every time you run this code, it will overwrite what is already there.

To re-flash your code, you will need to click the ‘files’ button on your taskbar again, to get access to the ‘flash’ button.

To open a file as read-only, and see the contents, you can use the following::

    with open('hello.txt') as my_file:
        content = my_file.read()
    print(content)


After flashing your new code, you will need to click the ‘repl’ button on your taskbar, to be able to read the content being printed out into the console.
After you have the repl open, to activate it, press the reset button on the back of your micro:bit to run the code from the top.
The contents of your text file should now print out to the repl.

To make any further changes, you need to click the ‘repl’ button again, to close it, before you can flash new code to your micro:bit.

More info about the file storage on the micro:bit can be found in the documentation:

- https://microbit-micropython.readthedocs.io/en/latest/tutorials/storage.html
- https://microbit-micropython.readthedocs.io/en/latest/filesystem.html

Some examples of this code in use, can be found here: https://github.com/ScienceOxford/intro-to-programming/tree/master/week-2:

- temperature_reading.py – this reads the temperature of the micro:bit’s processor, and writes it to a file every second
- input_reading.py – this waits for input from the user (in the repl), and writes that to a file
- radio_reading.py – this waits for messages being sent over radio, and writes them to a file
- light_reading.py – this reads the light level on the micro:bit’s display, and writes it, along with a time indicator, to a file
- light_reading_no_overwrite.py – this adds to the above code so that you can tell it when to start taking data
