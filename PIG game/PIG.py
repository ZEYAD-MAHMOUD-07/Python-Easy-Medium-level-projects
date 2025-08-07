import random


def roll():
    roll = random.randint(1, 6)
    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("The number of players must be between 2 and 4.")
    else:
        print("You should enter a number.")

max_score = 50
player_scores = [0 for _ in range(players)]

# print(player_scores)

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!\n")
        current_score = 0

        while True:

            should_roll = input("Would you like to roll (y)?").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! \nTurn done!")
                break

            else:
                current_score += value
                player_scores[player_idx] += value
                print("You rolled a", value)

            print("Your score is:", current_score)
            if current_score >= 50 or player_scores[player_idx] >= 50:
                winner = player_idx + 1
                break

        print("Your total score is:", player_scores[player_idx])

print("The Winner is the player number", winner, "!\n       #CONGRATULATIONS#")
