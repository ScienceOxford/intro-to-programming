Getting started with a Sukoku solving program
-------------

*If you are more interested in creating sudoku puzzles than in solving them, switch to the Guizero instructions here: https://github.com/ScienceOxford/intro-to-programming/blob/master/week-5/guizero/set-up.rst*

Below is a link to someone else's solution to this problem, but it uses concepts we haven't covered during the course, and so will take some time to understand.

https://towardsdatascience.com/peter-norvigs-sudoku-solver-25779bb349ce

This is a complicated project for your first independent program, so run through the problem step by step, and try to get one thing working at once!

**Suggestion:**

Decide on how you will format your starting grid.
For example, take this sudoku puzzle:

https://www.websudoku.com/?level=1&set_id=9143034716

.. image:: _sudoku.PNG

Which could be written as lists in the following ways::

  start = [0, 6, 0, 0, 9, 0, 0, 4, 7
           0, 1, 7, 3, 0, 6, 0, 0, 0
           0, 0, 3, 0, 2, 4, 0, 0, 5
           0, 0, 1, 5, 0, 0, 0, 3, 0
           0, 0, 6, 0, 1, 0, 9, 0, 0
           0, 8, 0, 0, 0, 2, 4, 0, 0
           6, 0, 0, 9, 7, 0, 5, 0, 0
           0, 0, 0, 4, 0, 3, 7, 2, 0
           9, 7, 0, 0, 8, 0, 0, 6, 0]

  start = ['.', '6', '.', '.', '9', '.', '.', '4', '7'
           '.', '1', '7', '3', '.', '6', '.', '.', '.'
           '.', '.', '3', '.', '2', '4', '.', '.', '5'
           '.', '.', '1', '5', '.', '.', '.', '3', '.'
           '.', '.', '6', '.', '1', '.', '9', '.', '.'
           '.', '8', '.', '.', '.', '2', '4', '.', '.'
           '6', '.', '.', '9', '7', '.', '5', '.', '.'
           '.', '.', '.', '4', '.', '3', '7', '2', '.'
           '9', '7', '.', '.', '8', '.', '.', '6', '.']

Next step could be to give each of the squares a grid co-ordinate. See the URL above, and read from **'Squares'** through to **'The Cross Function'**. Stop when they begin to discuss list comprehensions - this increases the efficiency of code, but makes it less readable - for now, it is more important that you understand what is going on, than it is that your code is efficient!

You will now have a list of grid co-ordinates to compare to your sudoku puzzle.

Now, either read through the rest of the solution at the URL, or design your own solution to the problem - it can be a good idea to first write your solution down in *pseudocode* i.e. write down your solution in logic a computer can follow, but not in real Python.
