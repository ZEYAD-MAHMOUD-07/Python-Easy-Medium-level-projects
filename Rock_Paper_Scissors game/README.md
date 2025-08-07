# ✊✋✌ Rock, Paper, Scissors Game (Python)

A simple terminal-based implementation of the classic **Rock, Paper, Scissors** game where the user plays against the computer.

## 📌 Features

- Play rounds of Rock/Paper/Scissors
- Random computer choices
- Tracks number of wins for user and computer
- Case-insensitive user input
- Option to quit anytime by typing `Q`

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Save the script as `rock_paper_scissors.py`
3. Open your terminal and run:

```bash
python rock_paper_scissors.py
```

## 🎮 Gameplay Example

```
Type Rock/Paper/Scissors or Q to quit :rock
Computer picked scissors.
You win!

Type Rock/Paper/Scissors or Q to quit :paper
Computer picked rock.
You win!

Type Rock/Paper/Scissors or Q to quit :scissors
Computer picked rock.
You lost!

Type Rock/Paper/Scissors or Q to quit :q
You won 2 times.
The computer won 1 times.
Goodbye!
```

## 💡 Game Logic

- Rock beats Scissors  
- Scissors beats Paper  
- Paper beats Rock  
- Random computer choice via `random.randint(0, 2)`
- Score is tracked and shown at the end

## 📁 File Structure

```
rock_paper_scissors.py    # Main game script
```

## 🛠 Notes

- User input is handled with `.lower()` to accept any case (e.g., "ROCK", "Rock", etc.)
- The game will **continue looping until** the user types `q`.

## 🧠 Challenge Yourself

- Add a "Draw" condition when both picks are the same.
- Add a round counter or best-of system.
- Turn it into a GUI game using `tkinter` or `pygame`.

## 📜 License

Free to use and modify.

