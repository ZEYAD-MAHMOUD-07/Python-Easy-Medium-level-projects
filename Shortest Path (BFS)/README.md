# 🧭 BFS Maze Solver with Python & Curses

This is a terminal-based pathfinding visualizer that uses **Breadth-First Search (BFS)** to find the shortest path in a maze. The maze is drawn using the `curses` library.

## 🧱 Maze Design

- `#` : Wall  
- ` ` : Empty space  
- `O` : Starting point  
- `X` : Target/Ending point  
- `*` : The path found by the algorithm (rendered in **red**)

## 🧠 Algorithm

The program uses the **Breadth-First Search (BFS)** algorithm to find the shortest path from the starting point `O` to the destination `X`.  
It animates the path exploration step by step with a short delay.

## 🖥 How It Looks

```text
#####O###
#       #
# ## ## #
# #   # #
# # # # #
# # # # #
# # # ###
#       #
#######X#
```

(The `*` characters will overlay this grid in red as the algorithm runs.)

## 🐍 How to Run

1. **Make sure you’re using a terminal that supports curses** (Linux/macOS. On Windows, use Git Bash or Windows Terminal).  
2. Save the code into a file called `maze_bfs.py`.  
3. Run the program:

   ```bash
   python maze_bfs.py
   ```

> 🪟 **Note for Windows users:** You may need to install `windows-curses` first:  
> ```bash
> pip install windows-curses
> ```

## 📁 File Structure

```
maze_bfs.py        # Main game code with pathfinding logic
```

## 🔍 Key Functions

- `find_start(maze, start)` – Locates the position of `O`.  
- `find_neighbors(maze, row, col)` – Returns valid neighbor cells (up/down/left/right).  
- `find_path(maze, stdscr)` – BFS search and visualization.  
- `print_maze(maze, stdscr, path)` – Prints the maze and shows the path step by step.

## 🧪 Customize It

- Add diagonal movement.  
- Change the maze structure.  
- Use DFS instead of BFS.  
- Speed up/slow down the animation using `time.sleep()`.

## 📜 License

Free to use and learn from.

