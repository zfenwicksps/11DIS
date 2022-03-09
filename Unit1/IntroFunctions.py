# Checks for a number in a range
# num = int(input("Enter a number: "))
def rangecheck(num): # this is called a function declaration
    min = 0
    max = 100
    for i in range (min,max): # loop that continues for a known number of iterations
        # print(i)
        if num > min and num < max: # conditional statement
            print(num)
            break
        else:
            print(f"Number {num} not in range {min} - {max}")
            break

# Once I have declared/created a function, I need to make a FUNCTION CALL
rangecheck(50)
rangecheck(120)
for i in range(50):
    a = i
    b = i * 10
    rangecheck(a)
    rangecheck(b)
    a += 1
    b -= 1
