import random


class MyClass:
    message = "My name is "
    name = ""

    def function(self):
        print("This is a message inside the class.")


x = MyClass()

num = random.randint(1, 3)

if num == 1:
    x.name = "Dean"
elif num == 2:
    x.name = "Matt"
else:
    x.name = "Alex"

print(x.message + x.name)
