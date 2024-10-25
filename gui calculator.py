import tkinter as tk

# Function to update the expression
def press(num):
    current_expression = equation.get()
    equation.set(current_expression + str(num))

# Function to evaluate the final expression
def equal_press():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set(" math error ")

# Function to clear the expression
def clear():
    equation.set("")

# Main GUI
if __name__ == "__main__":
    # Create window
    gui = tk.Tk()
    gui.title("Basic Calculator")
    gui.geometry("320x420")

    # StringVar to store the equation
    equation = tk.StringVar()

    # Textbox to display the equation
    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20), bd=10, justify='right')
    expression_field.grid(columnspan=4, ipadx=10, ipady=20)

    # Number buttons
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    # Create buttons and add them to the grid
    row = 1
    col = 0
    for button in buttons:
        if button == "=":
            tk.Button(gui, text=button, fg="black", width=10, height=3, bd=5,
                      command=equal_press).grid(row=row, column=col, columnspan=2)
            col += 2
        else:
            tk.Button(gui, text=button, fg="black", width=10, height=3, bd=5,
                      command=lambda b=button: press(b)).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Clear button
    tk.Button(gui, text="Clear", fg="black", width=22, height=3, bd=5, command=clear).grid(row=row, column=0, columnspan=4)

    # Start the GUI event loop
    gui.mainloop()
