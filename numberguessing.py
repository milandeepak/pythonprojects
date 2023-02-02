import random
i=0
n=random.randint(1,100)
while i==0:
    num=int(input("Guess the number(1,100) :"))
    if n==num:
        print("Whoa, You guessed number correctly")
        print(f"The number was {n}.")
        i=1
    else:
        print("OOOOOH,You guessed the wrong number ")
        diff=abs(num-n)
        print(f"You are {diff} unit away from Number!!")
        print("Try Again!")

