# Exercise 1: Profit Margin Calculator
# Asks for revenue and cost, then prints the profit and the profit margin.


def main():
    # Convert user input to float so we can handle cents (e.g., 5000.50)
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))

    profit = revenue - cost

    # Only calculate margin if revenue is positive (avoids dividing by zero)
    if revenue > 0:
        margin = (profit / revenue) * 100
        # :,.2f adds comma separators and rounds to 2 decimals
        print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
    else:
        print("Invalid revenue.")


main()
