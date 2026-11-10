import math

def calculate_fib4(age, ast, alt, platelets):
    for name, value in [("age", age), ("AST", ast), ("ALT", alt), ("platelets", platelets)]:
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
    return (age * ast) / (platelets * math.sqrt(alt))
