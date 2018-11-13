Creating a graph
-------------

Now that you have some clean data, you can use the Python library *matplotlib* to plot graphs.

This library is not installed by default.
The following instructions will install *matplotlib* on the computer you are using (currently a Raspberry Pi), and requires Python3 installed.
You may or may not have Python3 installed on your home computer - see seperate instructions for how to do this.

Open the terminal by clicking this icon:

.. image:: _terminal.PNG

Type the following command::

    pip install matplotlib

.. image:: _pip_install.PNG

The install process might take a long time! You can continue to work on your program while it is installing.
When it has finished, *matplotlib* is now installed on this computer.

You will be creating a graph from some of your cleaned data.
The following example shows a graph being created from a dictionary, where both keys and values are integers.

Firstly, at the top of your program::

    import matplotlib.pyplot as plt

This imports the library, and also renames it for this program, so that you can type plt whenever you would normally type matplotlib.pyplot

Now, underneath the code you have written to create a dictionary, try this example code::

    x = dictionary.keys()                 # set the values for the x and y axis
    y = dictionary.values()               # dictionary is the name of *your* created dictionary
   
    plt.plot(x, y)                        # make a plot of these values
  
    plt.xlabel('time')                    # labelling the axis
    plt.ylabel('light-reading')
  
    plt.title('Light reading over time')  # titling the graph
  
    plt.show()                            # show the graph - opens as an image

This code was modified from the below website, which has other useful examples:
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

The official documentation for the *matplotlib* library can be found here:
https://matplotlib.org/tutorials/introductory/pyplot.html
