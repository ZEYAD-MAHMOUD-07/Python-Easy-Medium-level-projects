# 🔐 Password Manager (Python + Cryptography)

A basic yet secure password manager built in Python using the `cryptography` library. This tool allows you to **safely store encrypted passwords** for different accounts, and view them only after decrypting using a key stored locally.

## 📌 Features

- Add and store encrypted passwords  
- View and decrypt saved passwords  
- Stores data in a local file (`password.txt`)  
- Uses symmetric encryption via the `Fernet` module from the `cryptography` library  
- Simple terminal interface (view, add, or quit)

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `cryptography` module

Install the cryptography module if you don’t have it:
```bash
pip install cryptography
```

### 🛠 Key Setup (Run Once)

Before using the password manager for the first time, you need to generate the encryption key:

```python
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
```

This creates a file called `key.key` which is essential for encryption and decryption. Keep this file safe — without it, passwords can't be recovered.

### 🔧 How to Use

1. Run the script:
```bash
python password_manager.py
```

2. Choose a mode:
   - `add` to add a new account and password
   - `view` to see all saved accounts and decrypted passwords
   - `q` to quit the program

## 📁 File Structure

```
password_manager.py    # Main script
password.txt           # Stores account names and encrypted passwords
key.key                # Encryption key used for Fernet
```

## 🧪 Sample Interaction

```
Would you like to add a new password or view existing ones (view/add), press q to quit? add  
Account Name: gmail  
Password: mySecret123  

Would you like to add a new password or view existing ones (view/add), press q to quit? view  
User: gmail | Password: mySecret123
```

## 🔒 Security Notes

- Passwords are stored **encrypted** in the file using Fernet (symmetric encryption).  
- The key used for encryption and decryption is stored locally in `key.key`.  
- If `key.key` is deleted or lost, passwords cannot be decrypted.  
- Do **not share your key.key** or `password.txt` files publicly.

## 📜 License

This project is open-source and free to use.

