import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

from password_checker import check_password_strength
from encryption import encrypt_file
from decryption import decrypt_file

selected_file = ""


def browse_file(file_label):
    global selected_file

    file_path = filedialog.askopenfilename()

    if file_path:
        selected_file = file_path
        file_name = os.path.basename(file_path)
        file_label.config(text=f"Selected File : {file_name}")


def update_strength(event, password_entry, strength_label):

    password = password_entry.get()

    strength, color = check_password_strength(password)

    strength_label.config(
        text=f"Password Strength : {strength}",
        fg=color
    )


def toggle_password(password_entry, toggle_button):

    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Show")


def encrypt_action(status_label, password_entry):

    global selected_file

    if selected_file == "":
        messagebox.showerror(
            "Error",
            "Please select a file first."
        )
        return

    password = password_entry.get()

    if password == "":
        messagebox.showerror(
            "Error",
            "Please enter a password."
        )
        return

    try:

        encrypted_path = encrypt_file(
            selected_file,
            password
        )

        status_label.config(
            text="Status : File Encrypted Successfully",
            fg="green"
        )

        messagebox.showinfo(
            "Success",
            f"Encrypted File Saved Successfully!\n\n{encrypted_path}"
        )

    except Exception as e:

        messagebox.showerror(
            "Encryption Error",
            str(e)
        )


def decrypt_action(status_label, password_entry):

    global selected_file

    if selected_file == "":
        messagebox.showerror(
            "Error",
            "Please select an encrypted file."
        )
        return

    password = password_entry.get()

    if password == "":
        messagebox.showerror(
            "Error",
            "Please enter the password."
        )
        return

    try:

        decrypted_path = decrypt_file(
            selected_file,
            password
        )

        status_label.config(
            text="Status : File Decrypted Successfully",
            fg="blue"
        )

        messagebox.showinfo(
            "Success",
            f"File Decrypted Successfully!\n\n{decrypted_path}"
        )

    except Exception as e:

        messagebox.showerror(
            "Access Denied",
            str(e)
        )


def create_gui():

    root = tk.Tk()

    root.title("Secure File Protection System")

    root.geometry("850x600")

    root.configure(bg="#f4f6f9")

    root.resizable(False, False)

    title = tk.Label(
        root,
        text="Secure File Protection System",
        font=("Arial", 22, "bold"),
        fg="#0B3D91",
        bg="#f4f6f9"
    )

    title.pack(pady=20)

    password_label = tk.Label(
        root,
        text="Enter Password",
        font=("Arial", 12),
        bg="#f4f6f9"
    )

    password_label.pack()

    password_frame = tk.Frame(
        root,
        bg="#f4f6f9"
    )

    password_frame.pack(pady=5)

    password_entry = ttk.Entry(
        password_frame,
        width=35,
        show="*"
    )

    password_entry.pack(
        side="left",
        padx=(0, 5)
    )

    toggle_button = ttk.Button(
        password_frame,
        text="Show",
        width=8,
        command=lambda: toggle_password(
            password_entry,
            toggle_button
        )
    )

    toggle_button.pack(side="left")

    strength_label = tk.Label(
        root,
        text="Password Strength : Not Checked",
        font=("Arial", 11),
        bg="#f4f6f9"
    )

    strength_label.pack(pady=10)

    password_entry.bind(
        "<KeyRelease>",
        lambda event: update_strength(
            event,
            password_entry,
            strength_label
        )
    )
    file_label = tk.Label(
        root,
        text="Selected File : No file selected",
        font=("Arial", 11),
        bg="#f4f6f9"
    )

    file_label.pack(pady=10)

    browse_button = ttk.Button(
        root,
        text="Browse File",
        command=lambda: browse_file(file_label)
    )

    browse_button.pack(pady=10)

    button_frame = tk.Frame(
        root,
        bg="#f4f6f9"
    )

    button_frame.pack(pady=20)

    encrypt_button = ttk.Button(
        button_frame,
        text="🔒 Encrypt File",
        width=20,
        command=lambda: encrypt_action(
            status_label,
            password_entry
        )
    )

    encrypt_button.grid(
        row=0,
        column=0,
        padx=15
    )

    decrypt_button = ttk.Button(
        button_frame,
        text="🔓 Decrypt File",
        width=20,
        command=lambda: decrypt_action(
            status_label,
            password_entry
        )
    )

    decrypt_button.grid(
        row=0,
        column=1,
        padx=15
    )

    status_label = tk.Label(
        root,
        text="Status : Ready",
        font=("Arial", 11, "bold"),
        fg="green",
        bg="#f4f6f9"
    )

    status_label.pack(pady=20)

    footer = tk.Label(
        root,
        text="Developed using Python | Secure File Protection System",
        font=("Arial", 9),
        fg="gray",
        bg="#f4f6f9"
    )

    footer.pack(side="bottom", pady=10)

    root.mainloop()