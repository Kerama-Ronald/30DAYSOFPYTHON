

# ### Day 1: Python Basics
# Start by installing Python and a text editor. Learn the basics of Python, such as: 
#  variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

# #### Exercise
#Python CalcSimple Pyulator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 
import math 
input_one = int(input("Input Value 1 "))
input_two = int(input("Input Value 2 "))
sign = input("Input sign ")
if sign == "+" :
    sum = input_one + input_two
    print (f"Answer is {sum} ")
    
elif sign == "*":
    product = input_one * input_two
    print ( f"Answer is {product}")

elif  sign == "-" :
    subtraction = input_one - input_two
    print ( f"Answer is {subtraction}")
    
elif sign == "/" :
    division = input_one / input_two
    print ( f"Answer is {division}")

elif sign == "**" :
    power = input_one ** input_two
    print ( f"Answer is {power}")
    
elif sign == "//" :
    sqrt = math.sqrt(input_one)
    print ( f"Answer is {sqrt}")
