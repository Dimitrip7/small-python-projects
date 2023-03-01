import random

top_of_range = input("Enter your number ")      

if top_of_range .isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger then 0 ")
else:
    print("Please enter a number ")
guesses = 0
random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guesses = input("Enter your guess ")      

    if user_guesses .isdigit():
        user_guesses = int(user_guesses)

        if user_guesses <= 0:
            print("Please enter a number larger then 0 ")
    else:
        print("Please enter a number ")

    if user_guesses == random_number:
        print("You got it correcct !")
        break
    elif user_guesses > random_number:
        print("You were above the number! ")
        continue
    else:
        print("You were below the number ! ")

print("You got it in", guesses , " guesses")
