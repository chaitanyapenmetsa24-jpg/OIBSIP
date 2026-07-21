import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(random.choice(characters) for _ in range(length))

        password_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Copy Password
def copy_password():
    password = password_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.configure(bg="#0F172A")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 22, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Password Length",
    font=("Arial", 13),
    bg="#0F172A",
    fg="white"
).pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
length_entry.pack(pady=10)

tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    width=20,
    command=generate_password
).pack(pady=15)

password_var = tk.StringVar()

password_box = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 14),
    width=35,
    justify="center"
)
password_box.pack(pady=15)

tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="#10B981",
    fg="white",
    width=20,
    command=copy_password
).pack(pady=10)

footer = tk.Label(
    root,
    text="Developed by Chaitanya Varma",
    font=("Arial", 10),
    bg="#0F172A",
    fg="#94A3B8"
)
footer.pack(side="bottom", pady=15)

root.mainloop()