import random

easy_level = 10
hard_levle = 5

def guess_number(count):
    number = random.randint(1,100)
    print(f"random number is {number}")
    while count !=0 :
        print(f"count : {count}")
        guess_number = int(input ("Make a guess: "))
        if guess_number == number :
            print("You win")
            break
        elif guess_number > number :
            print("Too high")
            print("Guess again")
            count -= 1
            print(f"You have {count} attempts remaining to guess the number")
        else :
            print("Too low")
            print("Guess again")
            count -= 1
            print(f"You have {count} attempts remaining to guess the number")
    if count == 0:
        print("You lose")

level = input ("""Welcome to the number Guessing Game!
I'm thinking of a number between 1 and 100
Choose a difficulty. Type 'easy' or 'hard': """)

if level == "easy":
    print(f"You have {easy_level} attempts remaining to guess the number")
    guess_number(easy_level)
elif level =="hard":
    print(f"You have {hard_levle} attempts remaining to guess the number")
    guess_number(hard_levle)
else :
    print("You input incorrect word")

