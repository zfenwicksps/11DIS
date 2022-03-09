# Create a function that takes 2 numbers that MULTIPLIES them, returning the result
def multiply(a,b):
    c = a*b
    print(f"{a}*{b}= {c}")
# Create a function that takes 2 numbers that DIVIDES the second from the first, returning the result
def divide(a,b):
    c = a/b
    print(f"{a}/{b}= {c}")
# Create a function that takes 2 numbers that ADDS them, returning the result
def add(a,b):
    c = a+b
    print(f"{a}+{b}= {c}")
# Create a function that takes 2 numbers that SUBTRACTS the second from the first, returning the result
def subtract(a,b):
    c = a-b
    print(f"{a}-{b}= {c}")
# Create a function that takes 2 numbers that DIVIDES the second from the first, returning the remainder
def modulus(a,b):
    c = a%b
    print(f"{a}%{b}= {c}")
run = "y"

# FUCNTION CALLS
#multiply(3,7)
#divide(100,4)
#add(20,9)
#subtract(30,6)


print("WELCOME TO THE FUNCTIONS CALCULATOR")
while run == "y":
    #a = int(input("Enter first number: "))
    operation = input("Choose an operation (+ - * / %): ")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if operation == "+":
        add(a,b)
    elif operation == "-":
        subtract(a,b)
    elif operation == "*":
        multiply(a,b)
    elif operation == "/":
        divide(a,b)
    elif operation == "%":
        modulus(a,b)
    elif operation == "exit".lower():
        run = "n"
    print("")
    print("Type 'exit' to stop")
    #run = input("Type 'exit' to stop")
    #if
