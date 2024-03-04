import tkinter as tk
import random
import string

# Function to generate a password based on user input
def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    # Define character sets based on complexity level
    if complexity == "Simple":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    # Generate the password using random characters from the selected character set
    password = ''.join(random.choice(characters) for i in range(length))
    password_var.set(password)
    check_strength(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Radio buttons for complexity
complexity_var = tk.StringVar()
complexity_var.set("Simple")
simple_radio = tk.Radiobutton(root, text="Simple", variable=complexity_var, value="Simple")
simple_radio.grid(row=1, column=0, padx=10, pady=5)
medium_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium")
medium_radio.grid(row=1, column=1, padx=10, pady=5)
complex_radio = tk.Radiobutton(root, text="Complex", variable=complexity_var, value="Complex")
complex_radio.grid(row=1, column=2, padx=10, pady=5)

# Label to display generated password
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=('Arial', 12), wraplength=300)
password_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Label to display password strength
strength_label = tk.Label(root, text="Password Strength:", font=('Arial', 12))
strength_label.grid(row=3, column=0, padx=10, pady=5)
strength_var = tk.StringVar()
strength_var.set("")
strength_indicator = tk.Label(root, textvariable=strength_var, font=('Arial', 12))
strength_indicator.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, columnspan=3, padx=10, pady=10)

# Function to check the strength of the generated password
def check_strength(password):
    if len(password) < 8:
        strength_var.set("Weak")
        strength_indicator.config(fg="red")
    elif len(password) < 12:
        strength_var.set("Moderate")
        strength_indicator.config(fg="orange")
    else:
        strength_var.set("Strong")
        strength_indicator.config(fg="green")

# Run the application
root.mainloop()
