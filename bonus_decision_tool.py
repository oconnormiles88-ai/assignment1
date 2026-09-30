# Bonus Challenge: Integrated Decision Tool
# Combines revenue/cost analysis with product categories to suggest an investment move.
# Requires Python 3.10+ (uses match-case).


def main():
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))
    product = input("What's the product category? ").strip().lower()

    category = get_category(product)

    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profitable! Profit: ${profit:,.2f}")
        print(f"Category: {category} | Suggestion: {get_suggestion(category)}")
    elif revenue == cost:
        print("Break-even: no profit or loss.")
        print("Suggestion: Hold off on investing until margins improve.")
    else:
        loss = cost - revenue
        print(f"Not profitable. Loss: ${loss:,.2f}")
        print("Suggestion: Review pricing and costs before investing.")


def is_profitable(revenue, cost):
    # Returns a bool: True only if revenue is greater than cost
    return revenue > cost


def get_category(product):
    # Same matching logic as Exercise 5
    match product:
        case "electronics" | "gadget":
            return "High Margin"
        case _ if product.startswith("tech"):
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        case _:
            return "Uncategorized"


def get_suggestion(category):
    # Maps each margin category to an investment suggestion
    match category:
        case "High Margin":
            return "Reinvest - scale up this product line"
        case "Medium Margin":
            return "Maintain - keep current investment level"
        case "Low Margin":
            return "Optimize - cut costs before expanding"
        case _:
            return "Research - review the category before investing"


main()