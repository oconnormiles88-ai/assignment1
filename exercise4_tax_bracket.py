# Exercise 4: Tax Bracket Determiner
# Finds an income's tax bracket and estimates the tax owed.
# Assumption: a flat rate is applied to the whole income (matches the sample output).


def main():
    income = float(input("What's your annual income? "))

    if not is_valid_income(income):
        print("Invalid income.")
    else:
        bracket = get_tax_bracket(income)
        tax = income * get_tax_rate(income)
        print(f"Your bracket: {bracket}. Estimated tax: {round(tax, 2)}")


def is_valid_income(income):
    # Returns a bool: True if income is 0 or more
    return income >= 0


def get_tax_bracket(income):
    if income < 0:
        return "Invalid income."
    elif income < 50_000:
        bracket = "Low (10%)"
    elif income < 100_000:
        bracket = "Medium (20%)"
    else:
        bracket = "High (30%)"

    # Bonus: ternary + modulo. An even income (income % 2 == 0) is deduction eligible
    return bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket


def get_tax_rate(income):
    # Returns the rate as a decimal so it can be multiplied by income
    if income < 50_000:
        return 0.10
    elif income < 100_000:
        return 0.20
    else:
        return 0.30


main()