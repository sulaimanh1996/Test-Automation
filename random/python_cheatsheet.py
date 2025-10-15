# ===========================
# 🐍 PYTHON CHEAT SHEET
# ===========================

## print
# The print() function shows output in the terminal.
print("Hello World!")

# ---------------------------

## types of inputs

# String: text written inside quotes (" " or ' ')
# Adding strings together combines them.
print("9" + "10")

# Integer (int): a whole number
# Adding integers gives their mathematical sum.
print(9 + 9)

# Float: a number with decimals
# You can add integers and floats together.
print(9 + 9.5)

# ---------------------------

## math operations
# Standard math rules apply.
# Parentheses () change the order of operations.

print(9 * 9 - 5)
print(9 * (9 - 5))

# ---------------------------

## variables
# Variables store values that can be used later.
# You can combine (concatenate) strings or add numbers.
# You can’t add a string and an integer directly — convert using str() and int().
# Multiplying strings repeats them.
# f-strings allow combining text and variables easily.

name = "bih ahh"
greeting = "Welcome"
complete_greeting = name + " " + greeting

number_1 = 1
number_2 = 2

a = 3
b = "test"

d = 3 * a      
e = 3 * b      

print(complete_greeting)                   
print(number_1 + number_2)                 
print(complete_greeting + str(number_2))   
print(int("1") + int("1"))
print(d)                                   
print(e)                                   
print(f"{greeting} {name}")                
print(f"{greeting} {number_1}")            

# ---------------------------

## user input
# input enables you to input a variable value
# dont forget to add a _ at the end

#? user_name = input("What is your username? ")
#? print (f"{greeting} {user_name}")

# ---------------------------

## booleans
# True or False
# == equal to
# >= greater or equal to
# <= lesser or equal to
# != not equal to
# capital affects the results
# < less then
# > greater then

print (10==10)
print ("S" == "s")
print ("Simon" < "Simon")
print ("Simon" < "simon")

# ---------------------------

## conditional statements
# if condition says if this then this
# else is addition to if, that says if this isnt what you want then this happens
# while condition says while this is .. do this
# elif for more criteria than two (if - else)
# cant add two if's under each other
# cant add two else's under each other

a = 2
b = 3

if a < 10:
    print("more!")
else:
    print("thats enough")

while a != 10:
    print("add + 2")
    a += 2

if b == 10:
    print("strong boi!")
elif b == 9:
    print("mid boi")
elif b <= 8:
    print("weak boi")
else:
    print("error too weak")

# ---------------------------

## boolean logic
# and/pr operator you can chain condition
# math first is ()

a=3
b=4

print (a == 3 and b==4)
print ((a == 3 or b == 5) and b == 5) # False, calculates () first
print (True and True)   #True
print (True and False)  #False
print (False and False) #False

print (a == 3 or b == 8)
print (True or False) #True
print (True or True) #True
print (False or False) #False

# ---------------------------

## lists
