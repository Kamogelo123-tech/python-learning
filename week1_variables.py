# Weeek 1: Python Basics
# Created by Kamogelo



# Variables


# This program stores your name and prints a welcome message
your_name = "Kamogelo"
print("Welcome to python, "+ your_name)


print("Hello Python")
my_name = "Kamogelo"
age = 21
place = "Hospital View"
print("My name is", my_name)
print("I'm", age,"years old and i currently live in Kagiso, specifically at",place,"with my mom.")
print("I'm going to work with you for some to become a self taugt software engineer")

x,y,z = "Python" , "is" , "awesome"
print(x,y,z)


# Data types, if/else logic and user input - (Day 2)

# list []
# tuple ()
name = "Kamogelo"
age = 21
height = 1.83
is_learning = True

print("As i explained ealier that my name is",name,"and I am",age,'.'"I'm",height,"cm tall")
print("Am I learning?",is_learning)
print("What is the data type of height?",type(height))
print("What is the data type of age?",type(age))
print("What is the data type of name?",type(name))
print("What is the data type of is_learning?",type(is_learning))
print(type('21')) # class 'str'

print("I have questions for you now")
age_input = input("How old are you? ")

if age_input.isdigit():
    age = int(age_input)  # 👈🏾 Now we know the user's real age!

    if age >= 18:
        print("You're an adult. Welcome!")
    else:
        print("Come on, you're young")
else:
    print("Enter valid age")



print("Another one")
height_input = input("How tall are you? ")

if height_input.replace(".","",1).isdigit():
    height = float(height_input)  # 👈🏾 Now we know the user's real height!

    if height >= 1.83:
        print("You're tall! That's good.")
    elif height >= 1.75:
        print("Average, not bad")
    else:
        print("I'm sorry but you're short")
else:
    print("Enter valid height")








