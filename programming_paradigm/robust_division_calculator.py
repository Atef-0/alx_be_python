def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return num / denom
    except ValueError:
        return "Invalid input: Please provide numeric values."
    except ZeroDivisionError as e:
        return str(e)