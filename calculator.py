import math
from history import CalculatorHistory


class Calculator:
    def __init__(self) -> None:
        """Initialize the Calculator with a default formula of '0'."""
        self.formula = "0"
        self.history = CalculatorHistory()

    def is_last_char_operator(self) -> bool:
        """Check if the last character in the formula is an operator."""
        return len(self.formula) > 0 and self.formula[-1] in "+-*/^."

    def starts_with_negative(self) -> bool:
        """Check if the formula starts with a negative number."""
        return (
            self.formula.startswith("-")
            and len(self.formula) > 1
            and self.formula[1] in "0123456789"
        )

    def get_formula(self) -> str:
        """Return the current formula."""
        return self.formula

    def calculate(self, operation: str) -> None:
        """Perform calculator computations based on the selected operation.

        Args:
            operation (str): The calculator operation to be performed.

        Returns:
            None: The result is stored in the 'formula' attribute of the Calculator instance.
        """
        if operation == "C":
            self.formula = ""
        elif operation == "del":
            self.formula = self.formula[0:-1]
        elif operation == "=":
            self.formula = str(eval(self.formula))
        elif operation == "√":
            self.formula = str((eval(self.formula)) ** 0.5)
        elif operation == "∛":
            self.formula = str((eval(self.formula)) ** (1 / 3))
        elif operation == "n√":
            self.formula += "**(1/"
        elif operation == "%":
            self.formula = str((eval(self.formula)) / 100)
        elif operation == "^2":
            self.formula = str((eval(self.formula)) ** 2)
        elif operation == "^3":
            self.formula = str((eval(self.formula)) ** 3)
        elif operation == "^":
            if not self.is_last_char_operator():
                self.formula += "**"
        elif operation == "π":
            self.formula = str(eval(self.formula + "math.pi"))
        elif operation == "e":
            self.formula = str(eval(self.formula + "math.e"))
        elif operation == "cos":
            self.formula = str(math.cos(math.radians(eval(self.formula))))
        elif operation == "sin":
            self.formula = str(math.sin(math.radians(eval(self.formula))))
        elif operation == "tan":
            self.formula = str(math.tan(math.radians(eval(self.formula))))
        elif operation == "cot":
            self.formula = str(1 / math.tan(math.radians(eval(self.formula))))
        else:
            if self.formula == "0" or self.starts_with_negative():
                self.formula = ""
            elif operation in "+-*/.^" and (
                self.is_last_char_operator() or self.starts_with_negative()
            ):
                self.formula = self.formula[:-1]
            self.formula += operation
            if self.formula == ".":
                self.formula = "0."

    def save_to_history(self, formula: str, result: str) -> None:
        """Save the calculation to the history.

        Args:
            formula (str): The formula that was calculated.
            result (str): The result of the calculation.
        """
        self.history.add_to_history(formula, result)
