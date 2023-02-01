# write a program that simulates rolling a dice

import random, time, sys
i=0
def rotate_line():
    symbols = "|/-\\"
    for i in range(20):
        sys.stdout.write("\r" + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.1)
while(i!=1):
    print("Hi, Welcome to The Dice Roller")
    choice=int(input("Enter your choice \n1) Roll the dice\n2) Exit the program : "))
    if choice==1:
        print("Rolling the dice...")
        rotate_line()
        time.sleep(1)
        print("\nThe value is ",random.randint(1,6))

    elif choice==2:
        print("Thank you , Hope you had fun!!!")
        i=1
