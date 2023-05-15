

# ### Day 1: Python Basics
# Start by installing Python and a text editor. Learn the basics of Python, such as: 
#  variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

# #### Exercise
# thon CalcSimple Pyulator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)


while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
   

    choice = input("Enter choice (1-6): ")

   
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please try again.")
        continue

    num1 = float(input("Enter the first number: "))

    if choice == '6':
        if num1 < 0:
            print("Error: Cannot calculate square root of a negative number!")
        else:
            print("Result:", square_root(num1))
    else:
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))

    print()  