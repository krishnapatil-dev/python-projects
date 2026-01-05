import random
n = random.randint(1,20) # to generate a random no. from 1 to 20
a = -1
guesses = 1 # default guess
while(a != n):
    a = int(input("Guess the number : "))
    
    if(a > n):
        print("Lower number please.")
        guesses += 1

    elif(a < n): 
        print("Higher number please.")
        guesses += 1

print(f"You successfully guessed the number {n} in {guesses} attempts")