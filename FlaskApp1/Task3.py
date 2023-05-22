import random

uscore = 0
cscore = 0
n=True
# 1 = paper
# 2 = scissors
# 3 = rock
# 4 = lizard
# 5 = spock
while n:
    uinput = int(input("Enter 1-5: "))
    cinput = random.randint(1,5)
    if uinput == cinput:
        break
    else:
        if uinput == 1:
            uinput = "Paper"
            if cinput == 2 or cinput == 4:
                cscore += 1
            else:
                uscore += 1
        elif uinput == 2:
            uinput = "Scissors"
            if cinput == 3 or cinput == 5:
                cscore += 1
            else:
                uscore += 1
        elif uinput == 3:
            uinput = "Rock"
            if cinput == 2 or cinput == 5:
                cscore += 1
            else:
                uscore += 1
        elif uinput == 4:
            uinput = "Lizard"
            if cinput == 2 or cinput == 3:
                cscore += 1
            else:
                uscore += 1
        elif uinput == 5:
            uinput = "Spock"
            if cinput == 2 or cinput == 4:
                cscore += 1
            else:
                uscore += 1
    if cinput == 1:
        cinput = "Paper"
    elif cinput == 2:
        cinput = "Scissors"
    elif cinput == 3:
        cinput = "Rock"
    elif cinput == 4:
        cinput = "Lizard"
    elif cinput == 5:
        cinput = "Spock"
    print(f"Player: {uinput} CPU: {cinput}")

    print(f"Player: {uscore} CPU: {cscore}")
