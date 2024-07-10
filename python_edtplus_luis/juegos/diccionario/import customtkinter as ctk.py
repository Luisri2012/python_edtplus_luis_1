import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Python")
        self.geometry("300x400")
        self.resizable(False, False)

        self.display = ctk.CTkLabel(self, text="0", font=("Arial", 24))
        self.display.pack(pady=20)

        self.buttons = []
        for i in range(9, -1, -1):
            button = ctk.CTkButton(self, text=str(i), font=("Arial", 16), width=50, height=50, command=lambda x=i: self.add_to_display(x))
            self.buttons.append(button)

        self.buttons[0].place(x=100, y=300)
        for i in range(1, 10):
            self.buttons[i].place(x=(i-1) % 3 * 75, y=250 - (i-1) // 3 * 50)

        self.operators = ['+', '-', '*', '/']
        self.operator_buttons = []
        for operator in self.operators:
            button = ctk.CTkButton(self, text=operator, font=("Arial", 16), width=50, height=50, command=lambda x=operator: self.add_to_display(x))
            self.operator_buttons.append(button)

        self.operator_buttons[0].place(x=225, y=300)
        for i in range(1, 4):
            self.operator_buttons[i].place(x=225, y=250 - (i-1) * 50)

        self.equals_button = ctk.CTkButton(self, text="=", font=("Arial", 16), width=50, height=50, command=self.evaluate)
        self.equals_button.place(x=175, y=300)

        self.clear_button = ctk.CTkButton(self, text="C", font=("Arial", 16), width=50, height=50, command=self.clear_display)
        self.clear_button.place(x=50, y=300)

    def add_to_display(self, value):
        if self.display.cget("text") == "0":
            self.display.configure(text=str(value))
        else:
            self.display.configure(text=self.display.cget("text") + str(value))

    def evaluate(self):
        try:
            result = str(eval(self.display.cget("text")))
            self.display.configure(text=result)
        except:
            self.display.configure(text="Error")

    def clear_display(self):
        self.display.configure(text="0")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()