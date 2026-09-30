# DATA 4000: Python with AI – Exercises

Solutions for the functions, variables, and conditionals exercises in DATA 4000 (School of Business). Written in Python 3.10+ and tested in VS Code.

## How to Run

```
python exercise1_profit_calculator.py
```

Exercises 5 and the bonus use `match-case`, so they need **Python 3.10 or newer**.

## Exercises

### Exercise 1 – Profit Margin Calculator
Takes revenue and cost, then prints the profit and the profit margin. It prints "Invalid revenue." if revenue is 0 or negative.

```
What's the revenue? 5000.0
What's the cost? 3500.0
Profit: $1,500.00 | Margin: 30.00%
```

### Exercise 2 – Credit Score Evaluator
Sorts a credit score (300–850) into Excellent, Good, Fair, or Poor and decides loan eligibility. A ternary expression picks the follow-up message.

```
What's your credit score? 720
Good - Loan Approved with Review. Interest rate: Low
```

### Exercise 3 – Customer Greeting Formatter
`format_greeting(name, title="Customer")` cleans up the name with `strip()`, `title()`, and `split()`, then returns a greeting that uses the first name only. An empty name returns "Hello, Valued Customer!" As the optional extension, the user can enter a custom title or press Enter to keep the default.

```
What's your full name?   john doe
Title (press Enter to skip)?
Hello, John (Customer)!
```

### Exercise 4 – Tax Bracket Determiner
`get_tax_bracket(income)` returns the bracket, `get_tax_rate(income)` returns the rate, and `is_valid_income(income)` returns a bool. As the bonus, a ternary with modulo labels even incomes "Deduction Eligible".

```
What's your annual income? 75000.0
Your bracket: Medium (20%) (Deduction Eligible). Estimated tax: 15000.0
```

### Exercise 5 – Product Category Matcher
Uses `match-case` to assign a margin category. A guard (`case _ if product.startswith("tech")`) catches any product that starts with "tech".

```
What's the product name?  Tech Phone
Product: tech phone | Category: High Margin
```

### Bonus – Integrated Decision Tool
Combines the ideas above. It takes revenue, cost, and a product category. The helper `is_profitable()` returns a bool, and a second `match` statement suggests an investment move based on the category. It also handles break-even and loss cases.

```
What's the revenue? 10000
What's the cost? 6000
What's the product category? electronics
Profitable! Profit: $4,000.00
Category: High Margin | Suggestion: Reinvest - scale up this product line
```

## Assumptions

- **Numeric input:** users enter valid numbers. Error handling (try/except) hasn't been covered yet, so text input like "abc" will crash the program.
- **Exercise 2:** "Fair - Loan Conditional" is treated as *not* approved, so it prints "Seek credit improvement."
- **Exercise 4:** a flat rate is applied to the entire income, not tiered brackets. This matches the sample output (75,000 × 20% = 15,000).
- **Exercise 4 bonus:** "Deduction Eligible" is added for even incomes, which is why the sample run shows it for 75000.0.
- **Bonus tool:** revenue equal to cost is treated as break-even, separate from a loss.