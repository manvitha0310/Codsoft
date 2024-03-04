import tkinter as tk

# Function to evaluate the expression entered by the user
def calculate():
    try:
        # Evaluate the expression entered in the entry widget
        result_value = eval(entry.get())
        # Format the result to display a maximum of 2 decimal places
        formatted_result = "{:.2f}".format(result_value)
        result.set(formatted_result)
    except Exception as e:
        # If an error occurs during evaluation, display "Error"
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for user input
entry = tk.Entry(root, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")  # Span all columns

# Create buttons for digits 0-9
buttons_frame = tk.Frame(root)
buttons_frame.grid(row=1, column=0, columnspan=3)

for i in range(3):
    for j in range(3):
        # Digit buttons
        digit = i * 3 + j + 1  # Calculate the digit value
        btn = tk.Button(buttons_frame, text=str(digit), padx=20, pady=10,
                        font=('Arial', 12), command=lambda digit=digit: entry.insert(tk.END, str(digit)))
        btn.grid(row=i, column=j, padx=5, pady=5)  # Grid layout for buttons

# Special buttons: 0, ., =
zero_btn = tk.Button(buttons_frame, text="0", padx=20, pady=10,
                     font=('Arial', 12), command=lambda: entry.insert(tk.END, "0"))
zero_btn.grid(row=3, column=0, padx=5, pady=5)

decimal_btn = tk.Button(buttons_frame, text=".", padx=22, pady=10,
                        font=('Arial', 12), command=lambda: entry.insert(tk.END, "."))
decimal_btn.grid(row=3, column=1, padx=5, pady=5)

equals_btn = tk.Button(buttons_frame, text="=", padx=20, pady=10,
                       font=('Arial', 12), command=calculate)
equals_btn.grid(row=3, column=2, padx=5, pady=5)

# Operator buttons: +, -, *, /
operators = ['+', '-', '*', '/']
operators_frame = tk.Frame(root)
operators_frame.grid(row=1, column=3, rowspan=4)

for i, operator in enumerate(operators):
    btn = tk.Button(operators_frame, text=operator, padx=20, pady=10,
                    font=('Arial', 12), command=lambda operator=operator: entry.insert(tk.END, operator))
    btn.grid(row=i, column=0, padx=5, pady=5)

# Button to clear the entry widget
clear_btn = tk.Button(operators_frame, text="Clear", padx=10, pady=10,
                      font=('Arial', 12), command=lambda: entry.delete(0, tk.END))
clear_btn.grid(row=len(operators), column=0, padx=5, pady=5)

# Label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=('Arial', 14))
result_label.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")  # Align to the top-right

# Run the application
root.mainloop()
