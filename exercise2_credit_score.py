# Exercise 2: Credit Score Evaluator
# Categorizes a credit score and decides loan eligibility.


def main():
    score = int(input("What's your credit score? "))

    # Check the valid range first (300-850) using the "or" logical operator
    if score < 300 or score > 850:
        print("Invalid score.")
    else:
        # Chained comparisons (e.g., 700 <= score < 750) check a range in one line
        if score >= 750:
            category = "Excellent - Loan Approved"
            approved = True
        elif 700 <= score < 750:
            category = "Good - Loan Approved with Review"
            approved = True
        elif 600 <= score < 700:
            category = "Fair - Loan Conditional"
            approved = False  # Assumption: conditional does not count as approved
        else:
            category = "Poor - Loan Denied"
            approved = False

        # Ternary expression picks the follow-up message
        message = "Interest rate: Low" if approved else "Seek credit improvement."
        print(f"{category}. {message}")


main()
