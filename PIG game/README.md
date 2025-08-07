# 🎲 Dice Game (Python)

A simple multiplayer dice rolling game for 2–4 players. Players take turns rolling a die and accumulating points. The first player to reach **50 points** wins!

## 📌 Features

- Supports 2 to 4 players  
- Each player rolls a 6-sided die on their turn  
- Rolling a 1 ends the player's turn and resets their turn score  
- Players can choose to stop rolling to keep their current points  
- First to reach 50 total points wins the game

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### 🔧 How to Play

1. Run the script:
```bash
python dice_game.py
```
2. Enter the number of players (2 to 4).
3. Each player takes turns rolling the die by typing `y`.
4. If a player rolls a 1, their turn ends with **0 points added**.
5. If they choose not to roll, their points for the turn are added to their total.
6. The game continues until one player reaches or exceeds 50 points.

## 📁 File Structure

```
dice_game.py       # Main Python script
```

## 🧪 Example Gameplay

```
Enter the number of players (2-4): 2

Player 1 turn has just started!

Would you like to roll (y)? y
You rolled a 5
Your score is: 5

Would you like to roll (y)? y
You rolled a 3
Your score is: 8

Would you like to roll (y)? n
Your total score is: 8

Player 2 turn has just started!

Would you like to roll (y)? y
You rolled a 1!
Turn done!
Your total score is: 0

...

The Winner is the player number 1!
       #CONGRATULATIONS#
```

## 🛠 Notes

- The game uses `random.randint(1, 6)` to simulate a real dice roll.
- Rolling a 1 at any point resets the **current turn's score** and ends the turn.
- To keep the score without risk, players can choose to **not roll**.

## 📜 License

This project is open-source and free to use.

