import tkinter as tk
from tkinter import messagebox

BUTTON_LAYOUT = (
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
)
WINDOW_TITLE = 'Calculadora'
WINDOW_SIZE = '300x400'
DISPLAY_FONT = ('Arial', 20)
BUTTON_FONT = ('Arial', 15)


class Calculator:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.expression = ''
        self.display_value = tk.StringVar()

        self.configure_root()
        self.create_display()
        self.create_buttons()
        self.create_control_buttons()

    def configure_root(self) -> None:
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)

    def create_display(self) -> None:
        display = tk.Entry(
            self.root,
            textvariable=self.display_value,
            font=DISPLAY_FONT,
            bd=10,
            insertwidth=4,
            width=14,
            justify='right',
        )
        display.grid(row=0, column=0, columnspan=4)

    def create_buttons(self) -> None:
        for row_index, row in enumerate(BUTTON_LAYOUT, start=1):
            for column_index, label in enumerate(row):
                self.create_button(
                    text=label,
                    row=row_index,
                    column=column_index,
                    command=lambda value=label: self.on_button_click(value),
                )

    def create_control_buttons(self) -> None:
        self.create_button(
            text='C',
            row=len(BUTTON_LAYOUT) + 1,
            column=0,
            command=self.clear,
            columnspan=2,
        )
        self.create_button(
            text='CE',
            row=len(BUTTON_LAYOUT) + 1,
            column=2,
            command=self.clear_entry,
            columnspan=2,
        )

    def create_button(
        self,
        text: str,
        row: int,
        column: int,
        command,
        columnspan: int = 1,
    ) -> None:
        button = tk.Button(
            self.root,
            text=text,
            padx=20,
            pady=20,
            font=BUTTON_FONT,
            command=command,
        )
        button.grid(row=row, column=column, columnspan=columnspan)

    def on_button_click(self, label: str) -> None:
        if label == '=':
            self.evaluate_expression()
            return

        self.append_character(label)

    def append_character(self, character: str) -> None:
        self.expression += character
        self.update_display()

    def evaluate_expression(self) -> None:
        try:
            self.expression = str(eval(self.expression))
            self.update_display()
        except (SyntaxError, ZeroDivisionError, TypeError, NameError):
            self.show_error()

    def show_error(self) -> None:
        messagebox.showerror('Erro', 'Expressão inválida')
        self.clear()

    def update_display(self) -> None:
        self.display_value.set(self.expression)

    def clear(self) -> None:
        self.expression = ''
        self.update_display()

    def clear_entry(self) -> None:
        self.expression = self.expression[:-1]
        self.update_display()


def main() -> None:
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == '__main__':
    main()