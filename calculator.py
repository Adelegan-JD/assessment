#This is question 1 solution
# Building a basic calculator
# Define all the functions for the arithmetic operations to be carried out(assition, subtraction, multiplication, and division)

# # Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for addition
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error! Division by Zero not possible.")

#Create a while loop that allows user select thier operation or exit the program
while True:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    try:
        choice = input("Choose operation (+, -, *, /) or 'exit' to quit: ")
        if choice == "exit":
            print("Exiting this calculator...\nGoodbye!")
            break
        elif choice =="+":
            print(f"The result of {num1} + {num2} is {add(num1, num2)}\n")
        elif choice == "-":
            print(f"The result of {num1} - {num2} is {subtract(num1, num2)}\n")
        elif choice == "*":
            print(f"The result of {num1} x {num2} is {multiply(num1, num2)}\n")
        elif choice == "/":
            print(f"The result of {num1} / {num2} is {divide(num1, num2)}\n")
        else:
            print("Invalid input. Please use 1 - 4 to carry out an operation or type \'exit\' to quit")
    except ValueError:
        print("Invalid input")

   




# This is question 2 solution
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")




# This question 3 solution

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break

    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")























