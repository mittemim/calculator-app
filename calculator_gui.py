import tkinter as tk
from calculator import add, subtract, multiply, divide, power

class CalculatorApp:
    """
    Класс для создания графического интерфейса калькулятора.
    """

    def __init__(self, root):
        """
        Инициализация графического интерфейса.
        """
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")

        # Поле для ввода и вывода результата
        self.display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
        self.display.grid(row=0, column=0, columnspan=4)

        # Кнопки калькулятора
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Расположение кнопок на сетке
        row = 1
        col = 0
        for button in buttons:
            tk.Button(
                root,
                text=button,
                font=("Arial", 15),
                width=5,
                height=2,
                command=lambda b=button: self.on_button_click(b)
            ).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Кнопка для очистки поля
        tk.Button(
            root,
            text="C",
            font=("Arial", 15),
            width=5,
            height=2,
            command=self.clear_display
        ).grid(row=row, column=col, columnspan=4)

    def on_button_click(self, button):
        """
        Обработка нажатия кнопок.
        """
        if button == "=":
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Ошибка")
        else:
            self.display.insert(tk.END, button)

    def clear_display(self):
        """
        Очистка поля ввода.
        """
        self.display.delete(0, tk.END)

def run_calculator():
    """
    Функция для запуска графического интерфейса калькулятора.
    """
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()