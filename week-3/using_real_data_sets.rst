Using real data sets
-------------

Now that you have practiced on some pre-prepared data, you can try downloading some real data sets to work from.

A good place to find data, is https://data.gov.uk/

The following example, uses a data set of schools in East Sussex, which can be downloaded from here:
https://data.gov.uk/dataset/e20e6581-1da4-46bb-94e8-bab86cd0e165/schools-in-east-sussex

The first thing to note, is that, until now, we have been working from .txt files.
Downloaded data is often found in .csv format, which stands for *comma-separated values*.

Each piece of data is seperated by a comma, which means that if we follow the same process as we did with the text files,
we will end up with every entry in a list, instead of every *line* in a list, which is less useful::
    
    [['School name'], ['School type'], ['Telephone'], ['Address1'], ['Address2'], ['Address3'], ['County'], ['Postcode'], ['Email'], ['Lower age'], ['Upper age'], ['Head Teacher'], ['Website']]
    !=
    ['School name', 'School type', 'Telephone', 'Address1', 'Address2', 'Address3', 'County', 'Postcode', 'Email', 'Lower age', 'Upper age', 'Head Teacher', 'Website']
    
Luckily, there is a Python library to help us work with csv files, and it comes pre-installed, so all we need to do is import it::

    import csv

    rows = []                                             # create an empty list to store each row

    with open('schools.csv') as csv_file:                 # open the file
        csv_reader = csv.reader(csv_file, delimiter=',')  # use the csv library to put the file in a format we can use
        for row in csv_reader:                            # iterate through each row
            rows.append(row)                              # append each row to our list
    
    print(rows)

You should now have your data stored as a list of lists - in each list, is all the data from a single row in the original file.

The next step, is to choose what data you actually want from this list.
For this example, we are going to compare the age range of each school.
We will do this by creating a dictionary with school name as the key, and the 'Lower age' and 'Upper age', stored in a tuple, as the value.

First step, print the values to make sure we are chosing the correct ones::

    dictionary = {}                                       # create an empty dictionary to store the chosen data

    for line in rows[1:]:                                 # iterate through each row *except* the first one, excluding it with [1:]
        print(line[0])                                    # print the 0th item in the list (school name)
        print((line[9], line[10]))                        # print the 9th and 10th items (ages) as a tuple, by placing them inside ()

This should print out information in the following way::

    'Alfriston School'
    ('5', '11')

Now, we want to add this to the dictionary, by replacing the above print statements.
For this to be more useful, we can also convert the ages from stings into integers::
    
    for line in rows[1:]:
        key = line[0]
        value = ((int(line[9]), int(line[10])))
        dictionary[key] = value

You should now have a dictionary in this format::

    {'Alfriston School':(5, 11), 'All Saints And St Richards Church Of England Primary School':(5, 11)}

You could now, for example:

- plot the upper and lower ages on a graph
- calculate the age range
- make a bar graph of number of schools that start at each age
- only show schools that take students within a certain age range
- etc, etc, etc!
