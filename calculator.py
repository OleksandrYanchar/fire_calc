import math


# Function to check if the last character in the formula is an operator
def is_last_char_operator(formula):
    if len(formula) > 0 and formula[-1] in "+-*/^.":
        return True
    return False


# Function to check if the formula starts with a negative number
def starts_with_negative(formula):
    return formula.startswith("-") and len(formula) > 1 and formula[1] in "0123456789"


# Counting function
def calculate(operation, formula):
    # Handling different calculator operations
    if operation == "C":
        formula = ""  # Clear the formula
    elif operation == "del":
        formula = formula[0:-1]  # Remove the last character from the formula
    elif operation == "=":
        formula = str(eval(formula))  # Evaluate the formula and update the result
    elif operation == "√":
        formula = str((eval(formula)) ** 0.5)  # Calculate square root of the formula
    elif operation == "∛":
        formula = str((eval(formula)) ** (1 / 3))  # Calculate cube root of the formula
    elif operation == "n√":
        formula += "**(1/"  # Add a placeholder for the n-th root operation
    elif operation == "%":
        formula = str((eval(formula)) / 100)  # Calculate percentage of the formula
    elif operation == "^2":
        formula = str((eval(formula)) ** 2)  # Calculate square of the formula
    elif operation == "^3":
        formula = str((eval(formula)) ** 3)  # Calculate cube of the formula
    elif operation == "^":
        if not is_last_char_operator(formula):
            formula += "**"  # Add the exponentiation operator to the formula
    elif operation == "π":
        formula = str(eval(formula + "math.pi"))  # Add the value of pi to the formula
    elif operation == "e":
        formula = str(
            eval(formula + "math.e")
        )  # Add the value of Euler's number (e) to the formula
    elif operation == "cos":
        formula = str(
            math.cos(math.radians(eval(formula)))
        )  # Calculate cosine of the formula (in degrees)
    elif operation == "sin":
        formula = str(
            math.sin(math.radians(eval(formula)))
        )  # Calculate sine of the formula (in degrees)
    elif operation == "tan":
        formula = str(
            math.tan(math.radians(eval(formula)))
        )  # Calculate tangent of the formula (in degrees)
    elif operation == "cot":
        formula = str(
            math.tan(math.radians(eval(formula)))
        )  # Calculate cotangent of the formula (in degrees)
    else:
        # Handling regular number and operator inputs
        if formula == "0" or starts_with_negative(formula):
            formula = ""
        elif operation in "+-*/.^" and (
            is_last_char_operator(formula) or starts_with_negative(formula)
        ):
            formula = formula[:-1]
        formula += operation
        if formula == ".":
            formula = "0."

    return formula
