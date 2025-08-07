import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = [
    "red",
    "blue",
    "yellow",
    "green",
    "orange",
    "purple",
    "black",
    "pink",
    "brown",
    "cyan",
]


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of the racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input , Please enter a Number.")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range (2-10). Try again")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT / 2:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    X_axis = WIDTH / (len(colors) + 1)
    # /	 Floating-point division	7 / 2 → 3.5	float
    # //	Integer (floor) division	7 // 2 → 3	int
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH / 2 + (i + 1) * X_axis, -HEIGHT / 2 + 20)
        turtles.append(racer)
    return turtles


def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


def main():
    racers = get_number_of_racers()
    init_screen()

    random.shuffle(COLORS)
    # Rearrange the list randomly
    colors = COLORS[:racers]
    # take the first racers items from the list
    print(colors, "\nEnter the color of your turtle from the choices: ")
    while True:
        user_turtle = input().lower()
        if colors.count(user_turtle) == 1:
            break
        else:
            print("Invalid input, choose from the list !")

    winner = race(colors)
    print("The winner turtle is the", winner, "one.")
    if user_turtle == winner:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
    
    time.sleep(12)


main()