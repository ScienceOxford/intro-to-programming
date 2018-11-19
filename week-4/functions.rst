Functions
-------------

Up until now, you have been writing code that runs through line by line.

By using functions, you can write a definition to explain how to do something. Then **call** that function later on in your program, when you actually want it to execute. 

For example, the following code does not use functions::

    name = input()
    print('Hello ' + name)

Compared to this, which does::

    def hello():
      name = input()
      print('Hello ' + name)
    
    hello()

The second is more efficient if you plan to do the same thing more than once.

Definitions must be written **before** they are called - your program is still being run line by line, and once your definition has been 'read' by the computer, it will be remembered and be useable throughout your program.

A longer example::

  def birthday():                           # defining a function called 'birthday'
    print('Happy birthday to you')
  
  birthday()
  birthday()
  print('Happy birthday dear Sarah')
  birthday()

---

Functions can also be defined with **arguments**.

print() is a function that takes an argument, whatever you put in the brackets will be printed.
When you want your function to take an argument, you must put a variable in the brackets of your definition, then tell it what to do with that variable.

For example, the following function takes an argument 'name'::

  def sing(name):                           # defining another function called 'sing' - this one takes an argument 'name'
    birthday()                              # here we call the birthday function defined above
    birthday()
    print('Happy birthday dear ' + name)
    birthday()
  
  sing('Sarah')                               # finially, we call the sing function, telling it what to use as the variable 'name'
