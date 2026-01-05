"""
Here,
1 = snake,
-1 = water,
gun = 0
"""
import random

computer = random.choice([1,-1,0])
youstr = input("Enter your choice : ")

youDict = {"snake" : 1,  "water" : -1, "gun" : 0}
reverseDict = {1 : "snake", -1 : "water", 0 : "gun"} 
you = youDict[youstr]

print(f"Your choosed {reverseDict[you]} <vs> Computer choosed {reverseDict[computer]}")

if(computer == you):
    print("Its a draw !!")
else:
    if(computer == 1 and you == -1):
        print("Computer won !!")

    elif(computer == 1 and you == 0):
        print("You won !!")

    elif(computer == -1 and you == 1):
        print("You won !!")

    elif(computer == -1 and you == 0):
        print("Computer won !!")

    elif(computer == 0 and you == 1):
        print("Computer won !!")
    
    elif(computer == 0 and you == -1):
        print("You won !!")

    else:
        print("Something went wrong.")

