# ===========================
# 🐍 PYTHON CHEAT SHEET
# ===========================

#!
##! print
#? The print() function shows output in the terminal.
# print("Hello World!")

# ---------------------------

#!
##! types of inputs
#? String: text written inside quotes (" " or ' ').
#? Adding strings together combines them (concatenation).
# print("9" + "10")  #? "910"

#? Integer (int): a whole number.
#? Adding integers gives their mathematical sum.
# print(9 + 9)  #? 18

#? Float: a number with decimals.
#? You can add integers and floats together.
# print(9 + 9.5)  #? 18.5

# ---------------------------

#!
##! math operations
#? Standard math rules apply.
#? Parentheses () change the order of operations.
# print(9 * 9 - 5)  #? 76
# print(9 * (9 - 5))  #? 36

# ---------------------------

#!
##! variables
#? Variables store values that can be used later.
#? You can combine (concatenate) strings or add numbers.
#? You can’t add a string and an integer directly — convert using str() or int().
#? Multiplying strings repeats them.
#? f-strings allow combining text and variables easily.

# name = "bih ahh"
# greeting = "Welcome"
# complete_greeting = name + " " + greeting

# number_1 = 1
# number_2 = 2

# a = 3
# b = "test"

# d = 3 * a       #? 9
# e = 3 * b       #? "testtesttest"

# print(complete_greeting)  #? "bih ahh Welcome"
# print(number_1 + number_2)  #? 3
# print(complete_greeting + str(number_2))  #? "bih ahh Welcome2"
# print(int("1") + int("1"))  #? 2
# print(d)  #? 9
# print(e)  #? testtesttest
# print(f"{greeting} {name}")  #? "Welcome bih ahh"
# print(f"{greeting} {number_1}")  #? "Welcome 1"

# ---------------------------

#!
##! user input
#? input() enables you to input a variable value.
#? Always ends with storing the input in a variable.
# user_name = input("What is your username? ")
# print(f"{greeting} {user_name}")  #? Greets the entered name

# ---------------------------

#!
##! booleans
#? True or False
#? == equal to        != not equal to
#? >= greater/equal   <= less/equal
#? <  less than       >  greater than
#? String comparison is case-sensitive.
# print(10 == 10)  #? True
# print("S" == "s")  #? False
# print("Simon" < "Simon")  #? False
# print("Simon" < "simon")  #? True (lowercase has higher code point)

# ---------------------------

#!
##! conditional statements
#? if: executes only if the condition is True
#? elif: adds more conditions (between if and else)
#? else: runs if nothing above was True
#? while: repeats as long as condition stays True
#? You can’t have two elses in one chain; multiple elif are fine.

# a = 2
# b = 3

# if a < 10:
#     print("more!")
# else:
#     print("that's enough")

# while a != 10:
#     print("add + 2")
#     a += 2

# if b == 10:
#     print("strong boi!")
# elif b == 9:
#     print("mid boi")
# elif b <= 8:
#     print("weak boi")
# else:
#     print("error: too weak")

# ---------------------------

#!
##! boolean logic
#? and/or operators let you chain conditions.
#? Use parentheses () to control order of operations.

# a = 3
# b = 4

# print(a == 3 and b == 4)  #? True
# print((a == 3 or b == 5) and b == 5)  #? False (parentheses first)
# print(True and True)   #? True
# print(True and False)  #? False
# print(False and False) #? False

# print(a == 3 or b == 8)  #? True
# print(True or False)  #? True
# print(True or True)  #? True
# print(False or False)  #? False

# ---------------------------

#!
##! lists
#? Make a list with []
#? If you add nothing, it’s an empty list. Separate items with commas.
#? Lists are ordered and can hold different data types.
#? You can put lists inside lists (nested lists).
#? Count starts at 0.
#? += adds elements to the list.
#? -= doesn’t exist — use remove() or pop() instead.

# a = [10, 1, 2, 3, 4, 3.56, "Hello", 10]
# b = []

# print(a.index(10))  #? Index of the first matching value (0)
# a.reverse()  #? Reverse in place (returns None)
# a.pop(1)  #? Remove item at index 1; pop() with no index removes last item
# a.append(99)  #? Add a value at the end
# print(a.count(10))  #? Count how many times 10 appears

# b = a.copy()  #? Shallow copy of list
# a.clear()  #? Remove all items
# a.extend(b)  #? Add items from another list
# a.insert(0, 1)  #? Insert value at a specific index

# print(a)  #? Show current list
# print(b)  #? Show copied list

# a += [45, 67, 77, "Sulaiman"]  #? Add multiple values at once
# print(a)  #? Show updated list

# a = [10, 1, 10, 2, 3, 4, 3.56, "Hello", [34, 56]]
# print(a[8][1])  #? Nested list indexing → 56

# ---------------------------

#!
##! Tuple
#? Make a tuple with ()
#? Very similar to a list, but immutable (cannot be changed).
#? Useful for fixed data that should not be modified.

# a = (23, 45.56, "Hello", [23, "Het"], (23, 90))
# print(a)  #? Show tuple

# ---------------------------

#!
##! Dictionaries
#? Key-value pairs using {} and "key": value format.
#? Keys: strings/ints/floats. Values: any type (string/list/tuple/dict/etc).

# a = {
#     "name": "Sulaiman",
#     "lastname": "Hashimi",
#     "age": 23,
#     "height": 177,
#     "list": [1, 2, 3],
#     "tuple": (4, 5, 6),
#     "dictionary": {"dictionary1": "input1", "dictionary2": "input2"}
# }
# print(a)  #? Show dict

# my_info = {"Name": "Sulaiman", "Age": 29}
# print(my_info)  #? Initial dict
# print(my_info.values())  #? Only values
# print(my_info.pop("Name"))  #? Remove key and return its value
# print(my_info)  #? After pop
# print(my_info.get("Age"))  #? Get value by key (None if missing)
# my_info.update({"Height": 177})  #? Add or update a key-value pair
# print(my_info.popitem())  #? Remove and return last (key, value) pair (LIFO)
# print(my_info)  #? Final dict

# ---------------------------

#!
##! For loops
#? The word after "for" can be anything (loop variable).
#? range() stops before the end number.
#? Example: range(5, 10) → 5,6,7,8,9

# for item in "Hello":  #? Each letter
#     print(item)

# for item in range(5, 10):
#     print(item)  #? 5 6 7 8 9

# names = ["Sulaiman", "Tabasom", "Jan"]

# for thiscanbeanything in names:
#     print(thiscanbeanything)  #? Prints each name

# for name in names:
#     print(f"Hello {name}!")
#     if name == "Sulaiman":
#         print("You bastard")
#         for name in names:
#             print("I'm inside the if clause")
#     elif name == "Tabasom":
#         print("You beauty")
#     else:
#         print("You random")

# ---------------------------

#!
##! While loops
#? while runs as long as the condition is True.
#? Stops when the condition becomes False.

# a = 0
# while a != 10:
#     a += 1
#     print("1 added!")

# user_input = ""
# #? Repeats until you enter "9"
# while user_input != "9":
#     user_input = input("Guess a number between 1 and 10: ")
#     if user_input != "9":
#         print("Wrong buddy")
#     elif user_input == "9":
#         print("You got the right number!")

# ---------------------------

#!
##! Functions
#? Start with "def".
#? Give your function a name followed by ().
#? Code inside runs when you call it later.
#? print() is also a function (built-in).
#? Use parameters to pass data into the function.
#? "\n" adds an empty line in print.

# def greeting_9():
#     print("Hello World!")

# greeting_9()  #? Call the function

# def greeting_9(name):
#     print(f"Hello {name}!")

# greeting_9(name=input("What is your name? "))  #? Pass an argument

#? Example game function with parameters
# def game_1(secret_number, user_input, stop_chars):
#     while user_input != stop_chars:
#         user_input = input("\n\nGuess a number between 1 and 100: ")
#         if user_input == secret_number:
#             print("You got the right number!")
#         elif user_input == "stop":
#             print("You wanted to stop.")
#         else:
#             print(f"The number is {user_input}. You got the wrong number, buddy!")

# game_1(
#     secret_number=input("Fill in your guessing number: "),
#     user_input='',
#     stop_chars="stop"
# )

# ---------------------------

#!
##! Returning values from functions
#? Use "return" to send values back from a function.
#? You can return multiple values separated by commas.
#? Function annotations can describe data types.

# a = 'hi'
# b = 45

# def sum_and_product_of(a: int, b: int) -> int:
#     return a + b

# c = sum_and_product_of("Hi", " There")  #? This will concatenate if not ints
# print(c)  #? Output depends on input types

# ---------------------------

#!
##! Classes
#? Class: a blueprint that lists rules (methods) and properties (attributes).
#? Class names usually start with a capital letter.
#? Create (instantiate) an object by calling the class with ().
#? Methods are functions inside the class; properties live on self.
#? Adding __init__ lets you pass values when creating the object.

# class Car:  #? Simple class with a class property
#     brand = ["Volvo", "Tesla"]  #? Class property shared by all instances

# car1 = Car()  #? Create an object from the class
# print(car1.brand[0])  #? Access property with dot notation
# car2 = Car()
# print(car2.brand[1])  #? Second item in the 'brand' list

# class Vehicle:
#     def __init__(self, brand, doors=4, wheels=4):  #? Initialize object
#         self.brand = brand
#         self.doors = doors
#         self.wheels = wheels

#     def car_greeting(self):  #? self refers to the current object
#         print("Hi, I'm your new car. My name is " + self.brand +
#               " and I have " + str(self.doors) + " doors, and " +
#               str(self.wheels) + " wheels!")

# vehicle1 = Vehicle("Volvo", 5, 5)  #? Custom values
# print(vehicle1.brand, vehicle1.doors, vehicle1.wheels)  #? Show properties
# vehicle1.car_greeting()  #? Call method

# vehicle2 = Vehicle("VW")  #? Uses default values
# print(vehicle2.brand)  #? You could also print inside the class itself

#!
##! Modules
#? if you want to run a function from a different file
#? module is a python file that can use functions in different files
#? see python_modules for the attached module

# import python.python_modules_for_cheatsheet as python_modules_for_cheatsheet   #you import that class from that module

# python_modules_for_cheatsheet.character_1