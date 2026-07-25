# 🔒 Secure File Protection System

A Python-based desktop application that securely encrypts and decrypts files using the **Cryptography (Fernet)** library. The project provides password-based file protection, password strength analysis, show/hide password functionality, and a user-friendly Tkinter graphical interface for secure file management.

---

## ✨ Features

- 🔒 Secure File Encryption
- 🔓 Secure File Decryption
- 🔑 Password-Based Protection
- 📊 Password Strength Checker
- 👁️ Show/Hide Password
- 📁 Browse Files
- 🖥️ User-Friendly Tkinter GUI
- ⚠️ Error Handling & Validation
- 📂 Automatic Encrypted & Decrypted File Management

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Cryptography (Fernet)
- PBKDF2 Password-Based Key Generation
- hashlib
- os

---

## 📁 Project Structure

```text
Secure_File_Protection_System/
│
├── main.py
├── gui.py
├── encryption.py
├── decryption.py
├── authentication.py
├── password_checker.py
├── encrypted_files/
├── decrypted_files/
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository.

```bash
git clone https://github.com/sharmichandran61-blip/Secure-File-Protection-System.git
```

2. Move into the project folder.

```bash
cd Secure-File-Protection-System
```

3. Install the required package.

```bash
pip install cryptography
```

4. Run the application.

```bash
python main.py
```

---

## 📖 How It Works

1. Launch the application.
2. Enter a secure password.
3. Check the password strength.
4. Browse and select a file.
5. Click **Encrypt File**.
6. The encrypted file is saved in the **encrypted_files** folder.
7. To decrypt, browse the encrypted file.
8. Enter the correct password.
9. Click **Decrypt File**.
10. The original file is restored in the **decrypted_files** folder.

---

## 🎯 Project Objective

The objective of this project is to protect confidential files using modern encryption techniques. It ensures that only authorized users with the correct password can decrypt and access the original files.

---

## 💻 Skills Demonstrated

- Python Programming
- GUI Development (Tkinter)
- Cryptography
- Password Security
- File Handling
- Exception Handling
- Desktop Application Development
## 📷 Screenshots

> Add screenshots of your application here.

- Home Screen
- Password Strength Checker
- Encryption Successful
- Decryption Successful


## 📜 License

This project is developed for educational and internship purposes.

---

## 👨‍💻 Author

**Sharmi Chandran**

Cyber Security Student

GitHub: https://github.com/sharmichandran61-blip

## ✅ Conclusion

The Secure File Protection System demonstrates the practical implementation of file encryption and decryption using Python. It combines cryptographic techniques with an intuitive graphical interface, helping users securely protect confidential files while promoting password security awareness.
