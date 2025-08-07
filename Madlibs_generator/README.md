# ✍️ Mad Libs Game (Python)

A simple Mad Libs-style word game where the user fills in placeholders in a story template to create a fun and personalized version of the story. The program reads a text file with placeholders, asks the user to provide words, and replaces those placeholders with their input.

## 📌 Features

- Reads a story from an external `.txt` file (`story.txt`)  
- Detects unique placeholders like `<place>`, `<verb>`, `<adjective>`  
- Prompts the user to fill in words for each placeholder  
- Replaces all placeholders with the user’s input  
- Prints the final, completed story

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A file named `story.txt` in the same directory as the Python script

### 🔧 How to Use

1. Make sure `story.txt` contains your story with placeholders (see example below).
2. Run the script:
```bash
python madlibs.py
```
3. The script will ask you to input values for each placeholder.
4. The final version of the story will be displayed with your inputs.

## 📄 story.txt Example

```
Today I went to the <place> with my <adjective> friend, <name>.  
We decided to <verb> near the <noun>.  
Suddenly, a <adjective> <animal> jumped out and scared us!  
I dropped my <object> and started to <verb>.  
It was the most <adjective> day ever!
```

## 🧪 Sample Run

```
Enter a word for <place> : beach  
Enter a word for <adjective> : funny  
Enter a word for <name> : Alex  
Enter a word for <verb> : dance  
Enter a word for <noun> : rock  
Enter a word for <animal> : monkey  
Enter a word for <object> : phone  

Today I went to the beach with my funny friend, Alex.  
We decided to dance near the rock.  
Suddenly, a funny monkey jumped out and scared us!  
I dropped my phone and started to dance.  
It was the most funny day ever!
```

## 🛠 Notes

- The script detects **unique placeholders only**. If a tag appears more than once (e.g. `<adjective>`), the same word will be used for all its occurrences.
- Make sure your placeholders are surrounded with `< >` brackets and do **not** include spaces.


## 📁 File Structure

```
madlibs.py        # Python script that runs the game  
story.txt         # Text file containing the story with placeholders  
```

## 📜 License

This project is open-source and free to use.

