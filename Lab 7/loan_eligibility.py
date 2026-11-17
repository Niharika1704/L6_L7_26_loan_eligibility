
import math

CATEGORIES = {
    "P": "Individual",
    "C": "Company",
    "H": "HUF",
    "F": "Firm"
}


def parse_income(income):
    if not isinstance(income, str):
        raise ValueError("Income must be a string")

    income = income.replace(",", "").strip()

    if not income.isdigit():
        raise ValueError("Invalid income")

    return int(income)


def monthly_emi(details):
    if not isinstance(details, str):
        raise ValueError("Details must be a string")

    parts = details.split(",")

    if len(parts) != 3:
        raise ValueError("Enter principal, rate and years")

    try:
        principal, rate, years = map(int, parts)
    except (ValueError, OverflowError):
        raise ValueError("All values must be integers")

    if principal <= 0:
        raise ValueError("Principal must be positive")

    if rate < 0:
        raise ValueError("Rate cannot be negative")

    if years <= 0:
        raise ValueError("Years must be positive")

    r = rate / 1200
    n = years * 12

    if r == 0:
        return round(principal / n, 2)

    try:
        emi = principal * r / (1 - (1 + r) ** (-n))
        result = round(emi, 2)
    except (OverflowError, ValueError):
        raise ValueError("EMI calculation failed")

    if not math.isfinite(result):
        raise ValueError("EMI calculation failed")

    return result


def pan_category(pan):
    if not isinstance(pan, str):
        raise ValueError("PAN must be a string")

    pan = pan.strip().upper()

    if len(pan) != 10:
        raise ValueError("PAN must contain 10 characters")

    category = pan[3]

    if category not in CATEGORIES:
        raise ValueError("Invalid PAN category")

    return CATEGORIES[category]


def main():
    print("==== Running parse_income ====")
    user_input = input("Enter monthly income (e.g. 50,000): ")
    result = parse_income(user_input)
    print("Income:", result)

    print("\n==== Running monthly_emi ====")
    user_input = input("Enter principal,rate,years (e.g. 500000,10,5): ")
    result = monthly_emi(user_input)
    print("Monthly EMI:", result)

    print("\n==== Running pan_category ====")
    user_input = input("Enter a PAN number (e.g. ABCPE1234F): ")
    result = pan_category(user_input)
    print("PAN Category:", result)


if __name__ == "__main__":
    main()
