import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
total_wrongs = 0
input("Press any button to start!")
print("--------------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()

    while True:

        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")

        if guess == str(answer):
            print("Correct\nYou got it after", wrong + 1, "times\n")
            print("-----------------------------------------------")
            wrong = 0
            break

        else:
            print("Wrong answer\nTry again\n")
            wrong += 1
            total_wrongs += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print(
    "--------------------------\nNice work!\nYou finished in",
    total_time,
    "seconds with",
    total_wrongs,
    "wrongs!",
)
