import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4."

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special_char = random.choice("!@#$%^&*()")

    all_characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    remaining_length = length - 4
    password = lowercase + uppercase + digit + special_char
    password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        generated_password = generate_password(length)
        result_var.set("Your password is: " + generated_password)
    except ValueError:
        result_var.set("Invalid input. Please enter a valid integer.")

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x150") 

# Configuring column and row weights to center-align widgets
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Widgets
length_label = ttk.Label(root, text="Enter password length:")
length_label.grid(row=0, column=0, pady=(20, 5), sticky=tk.E)

length_entry = ttk.Entry(root, width=3)
length_entry.grid(row=0, column=1, pady=(20, 5), sticky=tk.W)

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.grid(row=1, column=0, columnspan=1, pady=10, sticky=tk.E)

result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, wraplength=350, anchor=tk.W)
result_label.grid(row=2, column=0, columnspan=1, pady=(10, 20), sticky=tk.E)

# Run the Tkinter event loop
root.mainloop()
