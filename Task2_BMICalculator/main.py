import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100

        bmi = weight / (height * height)

        if bmi < 18.5:
            status = "Underweight"
            color = "#3498db"
        elif bmi < 25:
            status = "Normal Weight"
            color = "#2ecc71"
        elif bmi < 30:
            status = "Overweight"
            color = "#f39c12"
        else:
            status = "Obese"
            color = "#e74c3c"

        result.config(
            text=f"Your BMI: {bmi:.2f}\nCategory: {status}",
            fg=color
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result.config(text="", fg="white")


# ---------------- Window ---------------- #

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#0F172A")

# ---------------- Title ---------------- #

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 24, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Check your Body Mass Index",
    font=("Arial", 11),
    bg="#0F172A",
    fg="white"
)
subtitle.pack()

# ---------------- Weight ---------------- #

tk.Label(
    root,
    text="Weight (kg)",
    font=("Arial", 13, "bold"),
    bg="#0F172A",
    fg="white"
).pack(pady=(25, 5))

weight_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=20
)
weight_entry.pack()

# ---------------- Height ---------------- #

tk.Label(
    root,
    text="Height (cm)",
    font=("Arial", 13, "bold"),
    bg="#0F172A",
    fg="white"
).pack(pady=(20, 5))

height_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=20
)
height_entry.pack()

# ---------------- Buttons ---------------- #

calculate_btn = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 13, "bold"),
    bg="#2563EB",
    fg="white",
    width=18,
    command=calculate_bmi
)
calculate_btn.pack(pady=25)

reset_btn = tk.Button(
    root,
    text="Reset",
    font=("Arial", 13, "bold"),
    bg="#F59E0B",
    fg="white",
    width=18,
    command=reset
)
reset_btn.pack()

# ---------------- Result ---------------- #

result = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#0F172A",
    fg="white"
)
result.pack(pady=30)

# ---------------- Footer ---------------- #

footer = tk.Label(
    root,
    text="Developed by Chaitanya Varma",
    font=("Arial", 10),
    bg="#0F172A",
    fg="#94A3B8"
)
footer.pack(side="bottom", pady=15)

root.mainloop()