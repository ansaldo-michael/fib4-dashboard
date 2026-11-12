import math

def calculate_fib4(age, ast, alt, platelets):
    values = {"age": age, "AST": ast, "ALT": alt, "platelets": platelets}

    for name, value in values.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
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


def classify_fib4(score, age):
    low_cutoff = 2.0 if age >= 65 else 1.3
    if score < low_cutoff:
        return "Low"
    if score > 2.67:
        return "High"
    return "Indeterminate"


def get_warnings(age, ast, alt):
    warnings = []
    if age < 35:
        warnings.append("Age under 35: FIB-4 is less reliable in this age group.")
    if age >= 65:
        warnings.append("Age 65 or older: FIB-4 is less reliable; higher cutoffs are used.")
    if ast > 300:
        warnings.append("AST above 300 U/L: may indicate acute liver injury, where FIB-4 is unreliable.")
    if alt > 300:
        warnings.append("ALT above 300 U/L: may indicate acute liver injury, where FIB-4 is unreliable.")
    return warnings


def assess_fib4(age, ast, alt, platelets):
    score = calculate_fib4(age, ast, alt, platelets)
    category = classify_fib4(score, age)
    warnings = get_warnings(age, ast, alt)
    return {"score": score, "category": category, "warnings": warnings}
