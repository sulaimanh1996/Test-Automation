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
# make a list with []
# if you add nothing its an empty list, seperate with ,
# list is unordened 
# different datatypes in list
# you can add list in a list
# count starts with 0
# += adds to
# -= removes from

a = [10, 1, 2, 3, 4, 3.56, "Hello", 10]
b = []

print (a.index(10)) # returns the location of the given value
print (a.reverse()) # reverses the list
print (a.pop(1)) # removes the last value from the list of empty, else value given
print (a.append(99)) # adds value to your list as the last index
print (a.count(10)) # counts the number of the given values in the list
b = a.copy()    # copy's the content of the given list
print (a.clear())   # clears list
print (a.extend(b)) # extends list with content from another list
print (a.insert(0,1))   #inserts at location given value

print (a) 
print (b)

a += [45, 67, 77, "Sulaiman"]   # adds multiple values to list

print (a)

a = [10, 1, 10, 2, 3, 4, 3.56, "Hello", [34,56]]
print (a[8][1]) #finds value in list within a list (the 8 is where the list is and the one is the first value in that list)\

# ---------------------------

## Tuple
# make tuple with ()
# very simalir to list
# immutable (cant be changed)
# you can add everything in the tuple
# when you want set of data that cant be modified
# can only change if you reassasign whole value

a = (23, 45.56, "Hello", [23, "Het"], (23, 90))

print(a)

# ---------------------------

## Dictonaries
# looks like list and tuple
# make dictonary with {}
# format key value pair
# you can add list and tuple in this too
# keys can be string, integer or float
# value can be anything
# variable is key here

a = {
    "name":"Sulaiman", "lastname":"Hashimi", "age":23, "height":177, 
     "list":[1,2,3], 
     "tuple":(4,5,6), 
     "dictonary":{"dictionary1":"input1","dictionary2":"input2"}
     }

print (a)

my_info = {
    "Name":"Sulaiman",
      "Age":29
      }

print (my_info)
print (my_info.values()) # only shows values
print (my_info.pop("Name")) # removes the given value, give the key
print (my_info)
print (my_info.get("Age")) # gives the value of the given key
print (my_info.update({"Height":177})) # adds value to dictonary
print (my_info.popitem())   #pops the last record of the dictonary, you dont have to add anything
print 

print (my_info)