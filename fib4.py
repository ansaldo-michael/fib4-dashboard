import math

def calculate_fib4(age, ast, alt, platelets):
    values = {"age": age, "AST": ast, "ALT": alt, "platelets": platelets}

    for name, value in values.items():
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(f"{name} must be a real number")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    if not 18 <= age <= 120:
        raise ValueError("age must be between 18 and 120")
    if ast > 10000:
        raise ValueError("AST must be at most 10,000 U/L")
    if alt > 10000:
        raise ValueError("ALT must be at most 10,000 U/L")
    if platelets > 1000:
        raise ValueError("platelets must be at most 1000 x10^9/L")

    return (age * ast) / (platelets * math.sqrt(alt))
