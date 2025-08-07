# 🔐 Random Password Generator (Python)

A customizable password generator that creates secure passwords with a specified minimum length. The user can choose whether to include numbers and special characters.

## 📌 Features

- Choose the **minimum password length**  
- Optionally include **numbers** and/or **special characters**  
- Ensures password meets selected criteria  
- Uses `random` and `string` modules from Python standard library

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### 🔧 How to Use

1. Run the script:
```bash
python password_generator.py
```
2. Follow the prompts:
   - Enter the **minimum length** of the password
   - Choose whether to include numbers
   - Choose whether to include special characters
3. The script will generate and display a strong password that meets your criteria.

## 📁 File Structure

```
password_generator.py    # Main Python script
```

## 🧪 Sample Run

```
Enter the minimum length: 12  
Do you want to have numbers (y/n)? y  
Do you want to have special characters (y/n)? y  
The generated password is: w&Tb4pQMz!E@
```

## 🛠 Notes

- The generated password will always meet the selected requirements:
  - If numbers are enabled, at least one digit will be included.
  - If special characters are enabled, at least one special symbol will be included.
- The final password may exceed the minimum length depending on how soon all requirements are met.

## 🧠 Behind the Scenes

- `string.ascii_letters` provides uppercase and lowercase letters.
- `string.digits` adds numbers 0-9.
- `string.punctuation` includes characters like `!@#$%^&*()` and more.
- `random.choice()` is used to randomly pick characters.

## 📜 License

This project is open-source and free to use.

