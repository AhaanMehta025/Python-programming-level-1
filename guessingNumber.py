print("The guessing number game")


import random
number = random.randint(1,10)

name = input("What's your name?")
numOfGuess = 0
print("okay!", name, "I am choosing a number between 1 to 10. Try and guess it!")
print("You will get 5 chances to guess it!")

while numOfGuess<5:
    guess = int(input("make a guess!: "))
    
    if guess>number:
        print("too high")
    elif guess<number:
        print("too low")
    else :
        
        break
    numOfGuess+=1

if number == guess:
    print("Correct!")
else:
    print(f"You Lost!, the correct number was:  {number}")       



