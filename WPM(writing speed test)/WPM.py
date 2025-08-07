import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(
        0, 20, "Welcom to the Speed Typing Test!", curses.color_pair(1) | curses.A_BOLD
    )
    stdscr.addstr(1, 0, "Press any key to begin!", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}\n")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(3)
        if char != correct_char:
            color = curses.color_pair(4)

        stdscr.addstr(0, i, char, color)


def load_text():
    with open("Writing.txt", "r") as r:
        lines = r.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0

    start_time = time.time()
    stdscr.nodelay(True)

    while True:

        time_elapsed = round(max((time.time() - start_time), 1), 0)
        wpm = round((len(current_text) // (time_elapsed / 60)), 0)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):

            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            2,
            0,
            "You completed the test! Press any key to continue or Esc button to Exit.....",
        )
        key = stdscr.getkey()

        if ord(key) == 27:
            break


# (the first n empty lines , the first empty spaces , the phrase , the color and background color)


wrapper(main)
