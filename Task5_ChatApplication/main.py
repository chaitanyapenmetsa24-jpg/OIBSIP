import tkinter as tk
from tkinter import scrolledtext

def send_message(event=None):
    message = message_entry.get().strip()

    if message:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {message}\n")
        chat_area.insert(tk.END, "Bot: Thanks for your message!\n\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)
        message_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chat Application")
root.geometry("600x500")
root.configure(bg="#0F172A")
root.resizable(False, False)

title = tk.Label(
    root,
    text="💬 Chat Application",
    font=("Arial", 20, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    width=65,
    height=18,
    font=("Arial", 11),
    state=tk.DISABLED
)
chat_area.pack(padx=10, pady=10)

message_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=45
)
message_entry.pack(side=tk.LEFT, padx=(10, 5), pady=10, fill=tk.X, expand=True)

message_entry.bind("<Return>", send_message)

send_button = tk.Button(
    root,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    command=send_message
)
send_button.pack(side=tk.RIGHT, padx=(5, 10), pady=10)

root.mainloop()