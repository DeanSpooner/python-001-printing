# Python 001 - Printing, Variables, Classes, If/Else, Random

## print()

This prints whatever exists in the brackets, with quotation marks.

For example:

    print("My name is Dean.")

Will print in the terminal:

    My name is Dean.

## Variables

In Python, variables are simply declared as soon as they are named. Unlike JavaScript where **const** or **let** are used to first declare the variable, Python does not need anything like this. You simply name your new variable, followed by one equals sign then its value.

For example:

    name = "Dean"
    age = "31"
    print(name, age)

Will produce the following result in the terminal:

    Dean 31

## Concatenating strings

Just like JavaScript, multiple **string** variables can be printed or manipulated/concatenated together.

For example:

    print("My name is " + name + " and I am " + age + " years old.")

Will print:

    My name is Dean and I am 31 years old.

## Concatenating strings with ints

In the above example, **age** was a string. What if it was an integer?

    age = 31

By default, Python cannot concatenate this with a string.

For example:

    name = "Dean"
    age = "31"
    print("My name is " + name + " and I am " + age + " years old.")

Would result in an error:

    Exception has occurred: TypeError
    can only concatenate str (not "int") to str

Instead, a solution would be to use the **str()** method:

    print("My name is " + name + " and I am " + str(age) + " years old.")

Would give the desired result:

    My name is Dean and I am 31 years old.

## class MyClass:

You can create a new class by using the **class** keyword, followed by the name you give it and then a colon.

For example:

    class ExampleClass:

Will create a class called **ExampleClass**, which can then be used to create multiple objects with similar attributes and methods attached.

## class attributes

Classes have attributes which can easily be assigned.

For example:

    class Vehicle:
    	type = "bus"
    	colour = "red"
    	wheels = 4
    	seats = 50

Now if we create an object using this class...

    DeansBus = Vehicle()

This will have those same properties, e.g.:

    print(DeansBus.colour)

    red

Properties can be changed easily by redeclaring the object's property.

For example, using the **DeansBus** object we just created:

    DeansBus.colour = "blue"
    print(DeansBus.colour)

    blue

We were able to easily reassign the colour of **DeansBus** to be "blue".

New properties can also be added to the object easily...

    DeansBus.driver = "Dean"
    print(DeansBus.driver)

    Dean

## if elif

**If** statements can be used just like in JavaScript to set conditions for our code. We can also use **elif** as an _else if_ condition, and **else** as a final _else_ condition.

For example:

    num = 2

    if num == 1:
    	name = "Dean"
    elif num == 2:
    	name = "Matt"
    else:
    	name = "Alex"

    print(name)

Will always result in

    Matt

As that name falls under the **elif num == 2** condition.

## random.randint(x, y)

This is a method that can be used to select a random integer between and including **x** and **y**.

You must **import random** before running this.

For example:

    import random

    num = random.randint(1,4)

    print(num)

Will print 1, 2, 3 or 4 randomly each time it is ran.

This could be used in more creative ways such as:

    import random

    num = random.randint(1,3)

    if num == 1:
    	name = "Dean"
    elif num == 2:
    	name = "Matt"
    else:
    	name = "Alex"

    print(name)

This will print one of the names at random.

## input(prompt)

This provides some kind of prompt for the user to give an input. The input can be stored in a variable to be used later.

For example:

    userName = input("What is your name?")

    print("Hello, " + name + "!")

If I were to answer with _Dean_ for the input, the printed message would be:

    Hello, Dean!

## len(string)

This function measures the length of a string and returns an integer.

For example:

    len("Dean")

    4

Bear in mind, an **integer** and **not a string** is returned!
