# Euclid's Algorithm
# A (mod) B = C or A % B = C

#numbers = input("Enter 2 numbers... ")
#n = numbers.split(" ")
#a = int(n[0])
#b = int(n[1])
#try:
#    a = int(input("Enter a Number..."))
#    b = int(input("Enter a Number... "))
#except:
#    print("Please enter number as digits")
a = int(input("Enter a Number... "))
b = int(input("Enter a Number... "))
c = None
#print(1112%695)
while c != 0:
    c = a % b
    a = b
    b = c

print(a)

