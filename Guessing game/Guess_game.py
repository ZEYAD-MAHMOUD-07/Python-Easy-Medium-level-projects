import random

# r = random.randrange(0, 11)  # values between [0,10]
# r = random.randint(0, 3)  # values between [0,3]

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

rand_num = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Make a guess: ")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == rand_num:
        print("You got it")
        print("You needed " + str(guesses) + " times to get the correct guess (:")
        break
    else:
        print("oops!!\nTry again")
