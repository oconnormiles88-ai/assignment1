# Exercise 5: Product Category Matcher
# Uses match-case to sort a product into a pricing category.
# Requires Python 3.10+ (match-case was added in 3.10).


def main():
    # strip() removes extra spaces, lower() makes matching case-insensitive
    product = input("What's the product name? ").strip().lower()
    category = get_category(product)
    print(f"Product: {product} | Category: {category}")


def get_category(product):
    match product:
        # The | symbol means "or" inside a case
        case "electronics" | "gadget":
            return "High Margin"
        # A guard ("if ...") lets a case check a condition, like startswith()
        case _ if product.startswith("tech"):
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        # _ is the default case: runs if nothing above matched
        case _:
            return "Uncategorized - Review Needed"


main()

