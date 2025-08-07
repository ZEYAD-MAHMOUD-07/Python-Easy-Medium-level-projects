# ⌨️ Speed Typing Test (Terminal Game)

This is a terminal-based typing speed test game made using Python's `curses` module. It challenges your typing skills and calculates your **WPM (Words Per Minute)** in real-time.

---

## 🎮 Features

- Random sentence selection from a text file
- Live WPM calculation
- Color-coded character feedback:
  - ✅ Green for correct characters
  - ❌ Red for incorrect ones
- Backspace support
- Loop until you exit (with `Esc` key)

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Save the files as:

```
typing_test.py
Writing.txt
```

3. Run the game in the terminal:
```bash
python typing_test.py
```

> ⚠️ This game works only in **terminal environments** (not in IDLE or VS Code GUI).

---

## 📄 Writing.txt Format

This file should contain one sentence per line.

### 📝 Writing.txt
```
Hello world my name is Zeyad and I am the best at nothing!
This is another test block of text for this project!
Subscribe to Tech With Tim on YouTube.
Okay this is just another test to make sure the app is working okay!
The quick brown fox jumped over the rest of the sentence that I forget.
```

---

## 🖍️ Color Legend

- **Red & Bold**: Game title
- **Yellow**: Intro prompts
- **Green**: Correct characters
- **Red**: Incorrect characters

---

## 🛠 Dependencies

- `curses` (built-in for **Linux/macOS**)
- For **Windows**, run the following command:

```bash
pip install windows-curses
```

---

## 💡 Tips

- Press **Esc** at any time to quit the test.
- Use **Backspace** to fix mistakes.

---

## 🔖 License

This game is free to use and modify for educational purposes.

---

👨‍💻 Made with 💻 and `curses` in Python!

