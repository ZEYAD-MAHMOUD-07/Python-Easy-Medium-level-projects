name = input("Type your name: ")
print("Welcome", name, "to this adventure!")


answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go?"
).lower()


if answer == "left":

    answer = input(
        "You come to a river,do you want to walk around it or swim accross? Type walk to walk around and swim to swim accross :"
    ).lower()

    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print("Not a valid option! You lose.")


elif answer == "right":

    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head or back (cross/back)?"
    ).lower()

    if answer == "back":
        print("You go back and lose.")

    elif answer == "cross":

        answer = input(
            "You crossed the bridge and met a stranger. Do you want to talk to him?(yes/no)"
        ).lower()

        if answer == "yes":
            print("The stranger fucked you, You lose.")

        elif answer == "no":
            print("You ran away, and you found gold, You WIN.")

        else:
            print("Not a valid option! You lose.")

    else:
        print("Not a valid option! You lose.")

else:
    print("Not a valid option! You lose.")
