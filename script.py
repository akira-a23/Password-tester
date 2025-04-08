import tkinter as tk
from tkinter import ttk

def check_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak", "red", 20
    elif score <= 4:
        return "Medium", "orange", 60
    else:
        return "Strong", "green", 100

def check_button_clicked():
    password = password_entry.get()
    strength, color, bar_width = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}", foreground=color) # Changed 'fg' to 'foreground' here too, just in case!
    strength_bar.config(value=bar_width)
    strength_bar_label.config(text=f"{bar_width}%")

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    style = ttk.Style()
    style.configure("TCheck.TLabel", foreground="green")
    style.configure("TUncheck.TLabel", foreground="red")

    uppercase_indicator.config(style="TCheck.TLabel" if has_uppercase else "TUncheck.TLabel", text="Upper:")
    lowercase_indicator.config(style="TCheck.TLabel" if has_lowercase else "TUncheck.TLabel", text="Lower:")
    digit_indicator.config(style="TCheck.TLabel" if has_digit else "TUncheck.TLabel", text="Digit:")
    symbol_indicator.config(style="TCheck.TLabel" if has_symbol else "TUncheck.TLabel", text="Symbol:")

# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")

# Password entry field
password_label = ttk.Label(window, text="Enter Password:")
password_label.pack(pady=5)
password_entry = ttk.Entry(window, show="*")
password_entry.pack(pady=5)

# Check button
check_button = ttk.Button(window, text="Check Strength", command=check_button_clicked)
check_button.pack(pady=10)

# Strength bar
strength_frame = ttk.Frame(window)
strength_frame.pack(pady=5)
strength_bar = ttk.Progressbar(strength_frame, orient="horizontal", length=100, mode="determinate", maximum=100, value=0)
strength_bar.pack(side="left")
strength_bar_label = ttk.Label(strength_frame, text="0%")
strength_bar_label.pack(side="left", padx=5)

# Character type indicators
indicators_frame = ttk.Frame(window)
indicators_frame.pack(pady=5)
uppercase_indicator = ttk.Label(indicators_frame, text="Upper:")
uppercase_indicator.pack(side="left", padx=5)
lowercase_indicator = ttk.Label(indicators_frame, text="Lower:")
lowercase_indicator.pack(side="left", padx=5)
digit_indicator = ttk.Label(indicators_frame, text="Digit:")
digit_indicator.pack(side="left", padx=5)
symbol_indicator = ttk.Label(indicators_frame, text="Symbol:")
symbol_indicator.pack(side="left", padx=5)

# Result label
result_label = ttk.Label(window, text="Strength: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
