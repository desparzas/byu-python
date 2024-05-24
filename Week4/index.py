import random

while True:
    magic_number = random.randint(1, 100)
    counter = 0
    while True:
        

        
        user_guess = int(input("What is your guess?? "))
        counter += 1 
        if magic_number == user_guess:
            print("You guessed it!")
            break
        elif magic_number > user_guess:
            print("Higher")
        else:
            print("Lower")

    print(f"You used {counter} tries to find the right number :)")

    answer = input("Do you wanna play again?")
    answer = answer.lower()

    if answer != 'yes':
        break



    
