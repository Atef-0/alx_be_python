import random
random_number = random.randint(1,50)
guess = int(input("Guess a number between 1 and 50: "))
match guess:
    case _ if guess == random_number:
        print("GOLD GOLD GOLD")
    case _:
        print("Try again! The number was", random_number)