# Practice

# 1.Check whether a number is positive, negative or zero.

print("enter any number")
number = int(input())

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 2.Check whether a number is even or odd.

print("enter any number")
number = int(input())

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3.Check whether a person is eligible to vote.

print("enter an age")
age = int(input())

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 4.Find the greater of two numbers.

print("enter any number")
a = int(input())

print("enter any number")
b = int(input())

if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
else:
    print("Both are equal")


# 5.Check a student's grade based on marks.

print("enter marks")
marks = int(input())

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# 6.Check whether a person can enter a competition.
# Condition: age should be 18 or above.

print("enter age")
age = int(input())

if age >= 18:
    print("You can participate")
else:
    print("You cannot participate")


# 7.Simple login check.

username = "bhakti"
password = "python123"

if username == "bhakti" and password == "python123":
    print("Login successful")
else:
    print("Invalid username or password")


# 8.Find the largest among three numbers.

a = 25
b = 40
c = 30

if a >= b and a >= c:
    print("a is the largest")
elif b >= a and b >= c:
    print("b is the largest")
else:
    print("c is the largest")


# 9.Check whether a year is a leap year.

year = 2024

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


