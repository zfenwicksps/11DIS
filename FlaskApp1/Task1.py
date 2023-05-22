values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
roman = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
numberals = []
number = int(input("Input a number between 1 and 3999: "))
if 1 <= number <= 3999:
    for i in range(0, 13):
        while number >= values[i]:
            number = number - values[i]
            numberals.append(roman[i])

print(''.join(numberals))

# FOR TESTING
#print(numberals)
#print(type(values))
#print(type(roman))
#print(values[1])
#print(roman[1])
