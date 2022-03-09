def euclid(num):
        numbers = num.removeprefix("GCD")
        numbers = num.removeprefix("(")
        #n = numbers.split(")")
        numbers = numbers.removesuffix(")")
        n = numbers.split(",")

        a = int(n[0])
        b = int(n[1])
        c = None
        #print(1112%695)
        while c != 0:
            c = a % b
            a = b
            b = c
        print(a)
run = "y"
while run == "y":
    #numbers = input("Enter numbers following -> GCD(A,B)... ")


    numbers = input("Enter numbers following -> GCD(A,B)... ")
    euclid(numbers)
    run = input("Would you like to run again (y/n) ")
