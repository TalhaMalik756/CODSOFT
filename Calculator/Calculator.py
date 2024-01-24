import tkinter as tk
import math

# Colors / Fonts Initialization
Large_Font = ('Arial', 40, "bold")
Small_Font = ("Arial", 16)
Digits_Font = ("Arial", 24, "bold")
Default_font = ("Arial", 20)

Off_White = '#F8FAFF'
Light_Grey = '#F5F5F5'
Light_Blue = '#CCEDFF'
White = '#FFFFFF'
Label_Color = '#25265E'

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x500")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.label01, self.label = self.create_display_labels()
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

# Calling method init Button Frame
        self.button_frame = self.create_button_frame()
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

# Display Frame
    def create_display_labels(self):
        label01 = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                           bg=Light_Grey, fg=Label_Color, padx=24, font=Small_Font)
        label01.pack(expand=True, fill="both")

        label02 = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                           bg=Light_Grey, fg=Label_Color, padx=24, font=Large_Font)
        label02.pack(expand=True, fill="both")
        return label01, label02

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=200, bg=Light_Grey)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

# Button Frame
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=White, fg=Label_Color, font=Digits_Font,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=Off_White, fg=Label_Color, font=Default_font,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=Off_White, fg=Label_Color, font=Default_font,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2", bg=Off_White, fg=Label_Color, font=Default_font,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        try:
            value = float(self.current_expression)
            result = math.sqrt(value)
            self.current_expression = str(result)
            self.update_label()
        except ValueError:
            self.current_expression = "Error"
            self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax", bg=Off_White, fg=Label_Color, font=Default_font,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg=Light_Blue, fg=Label_Color, font=Default_font,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.label01.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()