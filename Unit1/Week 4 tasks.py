'''
DECLARE Integer a=5
DECLARE Integer b=2
DECLARE Integer c=3
DECLARE Integer result

SET result = a + b * c
DISPLAY result
result should equal 11

a=5
b=2
c=3

print(a+b*c)


DECLARE Integer num = 99
SET num = 5
DISPLAY num

num = 99
num = 5
print(num)


fave_food ASSIGNMENT ERROR and SYNTAX ERROR
DECLARE string favouriteFood
DISPLAY "What is the name of your favourite food"
INPUT favouriteFood
DISPLAY "Your favourite food is "
DISPLAY "favouriteFood"

first_prize ASSIGNMENT ERROR
DECLARE String 1stPrize
DISPLAY "Enter the award for first prize."
INPUT 1stPrize
DISPLAY "The first prize winner will receive", 1stPrize

average_score ARITHMETIC ERROR
DECLARE Integer lowest, highest, average 
DISPLAY "Enter the lowest score." 
INPUT lowest 
DISPLAY "Enter the highest score." 
INPUT highest 
SET average = low + high / 2 
DISPLAY "The average is ", average, "." 

Room_length SEQUENCE ERROR
DISPLAY "Enter the length of the room." 
INPUT length 
DECLARE Integer length 


favouriteFood = ""
print("What is the name of your favourite food")
favouriteFood = input("")
print("Your favourite food is")
print(favouriteFood)



firstPrize = ""
print("Enter the award for first prize.")
firstPrize = input()
print("The first prize winner will receive", firstPrize)




average_score
DECLARE Integer lowest, highest, average
DISPLAY "Enter the lowest score."
INPUT lowest
DISPLAY "Enter the highest score."
INPUT highest
SET average = low + high / 2
DISPLAY "The average is ", average, "."

'''
lowest = 0
highest = 0
average = 0
print("Enter the lowest score." )
lowest = int(input())
print("Enter the highest score." )
highest = int(input())
average = (lowest + highest) / 2
print("The average is", average, "." )
'''

print("Enter the length of the room.")
length = input()
print(f"Your room length is {length}.")


DECLARE string name
DECLARE string address
DECLARE string telephoneNumber
DECLARE string futureJob
INPUT what is your name
INPUT what is your address
INPUT what is your number
INPUT what is your futureJob
OUTPUT hello {name}
OUTPUT {name} lives in {address}
OUTPUT {name}'s number is {number}
OUTPUT {name} would like to become a {futureJob}
'''
name = ""
address = ""
telephoneNumber = ""
futureJob = ""
name = input("What is your name? ")
address = input("What is your address? ")
telephoneNumber = input("What is your telephone number? ")
print(f"Hello {name}.")
print(f"You live in {address}.")
print(f"Your camera phone camara thing number is {telephoneNumber}.")