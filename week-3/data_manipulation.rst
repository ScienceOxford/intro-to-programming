Data manipulation
-------------

This walkthrough uses the data set *light_sarah.txt*

Open Mu in Python 3 mode, and start a new file::

    my_file = open('light_sarah.txt')
    content = my_file.read()
    my_file.close()
    print(content)

Look at how the data is arranged - each piece of information on a seperate line.

Underneath this code, add the following::

    lines = content.split("\n")
    print(lines)

This creates a list, *lines*, and populates it with the content, but using the new line symbol as the break.
So each new line, gets a new entry in the list. See the difference between the two print statements.

Each line is a *string*, with two pieces of information in it – the time and the light reading.
We can split this again, to make another list – this time splitting with the comma, instead of the new line::

    for item in lines:
        items = item.split(",")
        print(items)

You can put anything inside the split function - whatever is in the speech marks is what it uses to separate the values.
You could use a space " ", a semicolon ";", whatever the data needs.

Look at the current data being printed.
It is mostly good, but the first line and the last line are not useful to us.

Items in a list can be accessed by their position in the list, and in Python, we start counting from 0.
So the first item in the list is [0], the next one [1], and so on.
You can also count from the end, the last item being [-1].

We can use this to modify the code like so::

    for item in lines[1:-1]:

This is now saying: for each item in lines, starting from item 1 (so skipping 0), 
and going up to **but not including** item -1 (the last item in the list).

Run it again, and see the difference printed out.
So if you needed to ignore the first two lines of the code, you’d say [2:-1].
If we want to keep the last line in this scenario, [2:]. If we ONLY wanted the first 5 lines, [0:6] **or** [:6].

Now we need to **do** something with this data – right now we’re printing it to the console, but not storing it anywhere.
To store the data in another new list, modify your code like so::

    data = []
    for item in lines[1:-1]:
        items = item.split(",")
        data.append(items)
    print(data)

This first creates an empty list, called data, then appends (or adds) each of the newly created lists into it.

So we have a list, called data, and each item in this list, is another list that contains two strings.
We are now going to remove unnecessary information from these strings, and pair the two values together in a dictionary.

Underneath all the previous code add::

    for element in data:
        key = element[0]
        value = element[1]
        print(key)
        print(value)

We can cut out the extra information from a string, the same way we took out the unnecessary items in the list before::

    key = element[0][7:]
    value = element[1][11:]
    
Or, alternatively::

    key = element[0].strip('time = ')
    value = element[1].strip(' reading = ')

These are still strings at the moment, which means we can’t use them for maths, or to plot a graph etc.
But now we have reduced them down to only the number information, we can convert them to integers::

    key = int(element[0][7:])
    value = int(element[1][11:])

Finally, we can now make our dictionary, which pairs the keys and values together, by modifying the code like so::

    dictionary = {}

    for element in data:
        key = int(element[0][7:])
        value = int(element[1][11:])
        dictionary[key] = value

    print(dictionary)
    
We have taken a long-winded process here, to show you all the different elements.
You won’t necessarily need to go through all of these steps for every data set,
take a look at what the data looks like, and decide what end format you would like.
