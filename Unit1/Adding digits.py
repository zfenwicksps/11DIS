# Adding digits

d = input("Enter a list of digits... ")
digits = []
num = "123456789"
number = 0
for dig in d:
#    if dig == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
     if dig in num:
        digits.append(dig)
#print(d)
for item in digits:
    number += int(item)
print(f"The sum of the given digits is {number}")



