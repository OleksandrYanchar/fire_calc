import tkinter as tk
import platform
from calculator import Calculator
from consts import buttons


class CalculatorApp:
    def __init__(self) -> None:
        """Initialize the CalculatorApp and set up the GUI."""
        self.root = self.create_gui()
        self.calculator = Calculator()
        self.label_text = self.create_display()
        self.create_buttons()

    def create_gui(self) -> tk.Tk:
        """Create the main GUI window."""
        root = tk.Tk()
        root.title("Calculator")
        root.geometry("850x805")
        # Check if running on Windows to set the icon
        if platform.system() == "Windows":
            root.iconbitmap("calculatorico.ico")
        root.resizable(False, False)
        root.wm_attributes("-topmost", 1)
        root.configure(bg="black")

        # Create a Text widget to display the calculation history
        self.history_text = tk.Text(
            root, font=("Roboto", 14), bg="white", fg="black", height=15, width=55
        )
        self.history_text.place(x=258, y=490)

        return root

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

    def update_history_text(self) -> None:
        """Update the calculation history displayed in the Text widget."""
        self.history_text.delete(1.0, tk.END)  # Clear the Text widget
        history = self.calculator.get_history()
        for formula, result in history:
            entry = f"{formula} = {result}\n"
            self.history_text.insert(tk.END, entry)

    def save_to_history(self) -> None:
        """Save the current calculation to the history."""
        formula = self.calculator.get_formula()
        result = self.label_text["text"]
        self.calculator.save_to_history(formula, result)
        self.update_history_text()

    def run(self) -> None:
        """Start the main window's event loop."""
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
