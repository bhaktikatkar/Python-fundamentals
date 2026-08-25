# Python Fundamentals - day 4
# Topic: Conditional Statements

# 1. if Statement
# --------------------------------------------------

age = 20

if age >= 18:
    print("You are eligible to vote.")


# --------------------------------------------------
# 2. if-else Statement

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# --------------------------------------------------
# 3. if-elif-else Statement

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# --------------------------------------------------
# 4. Multiple Conditions

age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry not allowed.")


# --------------------------------------------------
# 5. Nested if

has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("ID is required.")
else:
    print("You are not eligible.")



