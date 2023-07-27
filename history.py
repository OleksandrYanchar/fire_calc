class CalculatorHistory:
    def __init__(self):
        """Initialize the CalculatorHistory with an empty list to store history."""
        self.history = []

    def add_to_history(self, formula, result):
        """Add a new calculation record to the history.

        Args:
            formula (str): The formula that was calculated.
            result (str): The result of the calculation.
        """
        self.history.append((formula, result))

    def get_history(self):
        """Retrieve the entire history of calculations.

        Returns:
            list: A list of tuples, where each tuple contains (formula, result).
        """
        return self.history
