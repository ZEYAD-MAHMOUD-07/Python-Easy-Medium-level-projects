# ⏰ Alarm Timer (Python + Pygame)

A simple countdown timer that plays an alarm sound when the time is up. Built using Python and the `pygame` library.

## 📌 Features

- Set a custom countdown using minutes and seconds  
- Displays the remaining time in MM:SS format in the terminal  
- Plays an alarm sound (`alarm.mp3`) when the countdown ends  

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- Pygame library  

To install `pygame`, run:
```bash
pip install pygame
```

### 🔧 How to Use

1. Clone this repository or download the script.
2. Make sure you have an `alarm.mp3` file in the same directory.
3. Run the script:
```bash
python alarm_timer.py
```
4. Enter the number of minutes and seconds for the countdown.
5. Wait for the timer to reach 00:00 — the alarm will sound!

## 📁 File Structure

```
alarm_timer.py       # Main Python script  
alarm.mp3            # Alarm sound file (you must provide this)  
```

## 📷 Preview

```
How many minutes to wait: 0  
How many seconds to wait: 5  
00:05  
00:04  
00:03  
00:02  
00:01  
```

## 🛠 Notes

- The terminal uses ANSI escape codes to clear and update the time display. This works best in Unix-like terminals (e.g., Linux, macOS). On Windows, use a compatible terminal like Git Bash or Windows Terminal for proper formatting.
- To stop the alarm, you may need to manually close the script depending on your terminal.

## 📜 License

This project is open-source and free to use.

