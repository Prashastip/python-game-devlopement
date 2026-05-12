
# print("Hello word")
# for i in range (10,0,-1):
#     print(i)

# guessing game
import random
while True:
    num1=random.randint(1,50)
    num2=random.randint(50,100)
    sym=random.choice(["+","-","*"])
    ans = int(input("What is " + str(num1) + sym + str(num2) + "? "))

    if sym=="+":
        realans=num1+num2
    elif sym=="-":
        realans=num1-num2
    elif sym=="*":
        realans=num1*num2
    else: 
        print("Invalid choice")

    if ans==realans:
        print("Correct!")
    else:
        print("Incorrect! The answer was", realans)
    qu=input("Would you like to play again (yes/no)? ").lower()
    if qu!="yes":
        print("Game over")
        break


