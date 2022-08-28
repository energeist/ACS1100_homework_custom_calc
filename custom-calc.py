# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

#def calculate_volume (height, length, width):
#    result = height * length * width
#    return result

# str_number = input("Please enter a number: ")

# ===========================================================================================
 
# import regular expression module
import re

print(
"""
Welcome to my rectangular prism volume calculator!

This calculator will only accept positive integer and floating point values as valid input for dimension numbers
and text as valid input for your dimension.
""")

unit = input("What units of measurement are you providing? (cm, in, feet, etc.): ")

# check that unit input is a text string using regular expression
while not re.match("^[a-zA-z]+$", unit):
    print ("Error! Please enter an alphabetical text string (a-z or A-Z characters) for your units of measurement.\n")
    unit = input("Please enter a valid unit of measurement: ")
print(f"{unit} accepted as your unit of measurement.\n")

# define function to perform check for non-zero positive int/float input to reduce overall code length
def num_error_check(str_number, dimension):
    while re.match("[^0-9\.]*$", str_number) or float(str_number) <= 0:
        print ("Error! Please only use numeric characters to enter a non-zero positive value.\n")
        str_number = input(f"Please re-enter a valid number for {dimension}: ")
# cast the validated number as a float
    number = float(str_number)
    print(f"{number:.2f} {unit} accepted for {dimension}\n")
    return number

dimension = "height"
str_height = input(f"Please enter the {dimension} of the box: ")
height = num_error_check(str_height, dimension)

dimension = "width"
str_width = input(f"Please enter the {dimension} of the box: ")
width = num_error_check(str_width, dimension)

dimension = "length"
str_length = input(f"Please enter the {dimension} of the box: ")
length = num_error_check(str_length, dimension)

print(f"""
The dimensions you have submitted (rounded to two decimal places) are:
Height - {height:.2f} {unit}
Width - {width:.2f} {unit}
Length - {length:.2f} {unit}

The volume of your rectangular prism is {(height * width * length):.2f} {unit}^3.
""")
