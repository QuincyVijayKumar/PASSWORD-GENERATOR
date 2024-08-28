import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip

# Function to generate a random password
def generate_password():
    length = length_var.get()
    if length < 6:
        messagebox.showwarning("Weak Password", "Password length should be at least 6 characters for better security.")
        return

    char_set = ""
    if uppercase_var.get():
        char_set += string.ascii_uppercase
    if lowercase_var.get():
        char_set += string.ascii_lowercase
    if numeric_var.get():
        char_set += string.digits
    if symbols_var.get():
        char_set += string.punctuation
    
    if not char_set:
        messagebox.showwarning("No Characters Selected", "Please select at least one character type.")
        return

    password = "".join(random.choice(char_set) for _ in range(length))
    password_var.set(password)

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Function to update the length display label
def update_length_display(value):
    length_display_var.set(f"{int(float(value))}")

# Toggle between light and dark mode
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#1e1e1e")
        customize_frame.config(bg="#1e1e1e", fg="white")
        password_display.config(bg="#2e2e2e", fg="white")
        copy_button.config(bg="#2e2e2e", fg="white")
        generate_button.config(bg="#00cc44", fg="white")
        style.configure("TScale", background="#1e1e1e", troughcolor="#2e2e2e", sliderrelief="flat", sliderlength=15)
    else:
        root.config(bg="#f4f4f9")
        customize_frame.config(bg="#f4f4f9", fg="black")
        password_display.config(bg="white", fg="black")
        copy_button.config(bg="lightgray", fg="black")
        generate_button.config(bg="#4CAF50", fg="white")
        style.configure("TScale", background="#f4f4f9", troughcolor="lightgray", sliderrelief="flat", sliderlength=15)

# GUI Setup
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x400")
root.config(bg="#1e1e1e")  # Default dark background color

# Customization Section
customize_frame = tk.LabelFrame(root, text="Customize your password", font=("Helvetica", 12, "bold"), bg="#1e1e1e", fg="white", bd=2, relief="flat")
customize_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="we")

# Checkbox Options
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numeric_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(customize_frame, text="Uppercase", variable=uppercase_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12), selectcolor="#1e1e1e").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Checkbutton(customize_frame, text="Lowercase", variable=lowercase_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12), selectcolor="#1e1e1e").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Checkbutton(customize_frame, text="Numeric", variable=numeric_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12), selectcolor="#1e1e1e").grid(row=0, column=1, sticky="w", padx=10, pady=5)
tk.Checkbutton(customize_frame, text="Symbols", variable=symbols_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12), selectcolor="#1e1e1e").grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Password Length Slider
tk.Label(customize_frame, text="Password Length:", bg="#1e1e1e", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
length_var = tk.IntVar(value=12)
length_slider = ttk.Scale(customize_frame, from_=6, to_=30, orient="horizontal", variable=length_var, style="TScale", command=update_length_display)
length_slider.grid(row=2, column=1, padx=10, pady=10, sticky="we")

# Length Display Label
length_display_var = tk.StringVar(value="12")
length_display = tk.Label(customize_frame, textvariable=length_display_var, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
length_display.grid(row=2, column=2, padx=10, pady=10, sticky="w")

# Generate Button
generate_button = tk.Button(root, text="Generate", command=generate_password, bg="#00cc44", fg="white", font=("Helvetica", 14, "bold"), relief="flat", cursor="hand2")
generate_button.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="we")

# Password Display Area
password_var = tk.StringVar()
password_display = tk.Entry(root, textvariable=password_var, font=("Helvetica", 16), bg="#2e2e2e", fg="white", bd=2, relief="flat", justify="center")
password_display.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="we")

# Copy Button
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, bg="#2e2e2e", fg="white", font=("Helvetica", 12), relief="flat", cursor="hand2")
copy_button.grid(row=2, column=2, padx=10, pady=10)

# Dark/Light Mode Toggle Button
toggle_button = tk.Button(root, text="🌓", command=toggle_theme, bg="#1e1e1e", fg="white", font=("Helvetica", 14), relief="flat", cursor="hand2")
toggle_button.grid(row=0, column=3, padx=10, pady=20)

# Configure ttk Scale Style
style = ttk.Style()
style.configure("TScale", background="#1e1e1e", troughcolor="#2e2e2e", sliderrelief="flat", sliderlength=15)

# Dark mode flag
dark_mode = True

root.mainloop()
