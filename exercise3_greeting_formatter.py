# Exercise 3: Customer Greeting Formatter
# Cleans up a customer's name and returns a personalized greeting.


def main():
    name = input("What's your full name? ")

    # Optional extension: let the user enter a custom title
    title = input("Title (press Enter to skip)? ").strip().title()

    # If no title was given, rely on the function's default ("Customer")
    if title:
        print(format_greeting(name, title))
    else:
        print(format_greeting(name))


def format_greeting(name, title="Customer"):
    # strip() removes extra spaces at the start and end
    name = name.strip()

    # An empty string means no name was entered
    if name == "":
        return "Hello, Valued Customer!"

    # title() capitalizes the first letter of each word ("john doe" -> "John Doe")
    name = name.title()

    # split() breaks the name into words at spaces; [0] grabs the first word
    first_name = name.split()[0]

    return f"Hello, {first_name} ({title})!"


main()

