import tkinter as tk
import platform
from calculator import Calculator
from consts import buttons


class CalculatorApp:
    def __init__(self) -> None:
        """Initialize the CalculatorApp."""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("850x805")
        # Check if running on Windows to set the icon
        if platform.system() == "Windows":
            self.root.iconbitmap("calculatorico.ico")
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", 1)
        self.root.configure(bg="black")

        self.calculator = Calculator()
        self.label_text = self.create_display()
        self.create_buttons()

    def create_display(self) -> tk.Label:
        """Create a Label widget to display the calculator's formula."""
        label_text = tk.Label(
            self.root,
            text=self.calculator.get_formula(),
            font=("Roboto", 30, "bold"),
            bg="black",
            fg="white",
        )
        label_text.place(x=11, y=50)
        return label_text

    def create_button(self, text: str, x: int, y: int) -> None:
        """Create a calculator button with the specified text and position."""

        def get_label():
            self.calculator.calculate(text)
            self.label_text.configure(text=self.calculator.get_formula())

        tk.Button(
            self.root,
            text=text,
            bg="green",
            fg="white",
            font=("Roboto", 20),
            command=get_label,
        ).place(x=x, y=y, width=115, height=79)

    def create_buttons(self) -> None:
        """Create all the calculator buttons."""
        x, y = 18, 140
        for button in buttons:
            self.create_button(button, x, y)
            x += 117

            # Creating a new line of buttons if the previous one is full
            if x > 800:
                x = 18
                y += 81

    def run(self) -> None:
        """Start the main window's event loop."""
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
