# Python Fundamentals - Day 2
# Topic: Operators


# 1. Arithmetic Operators

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# --------------------------------------------------
# 2. Comparison Operators

x = 10
y = 20

print(x == y)   # Equal to
print(x != y)   # Not equal to
print(x > y)    # Greater than
print(x < y)    # Less than
print(x >= y)   # Greater than or equal to
print(x <= y)   # Less than or equal to


# --------------------------------------------------
# 3. Assignment Operators

num = 10

num += 5
print("After += :", num)

num -= 3
print("After -= :", num)

num *= 2
print("After *= :", num)

num /= 4
print("After /= :", num)


# --------------------------------------------------
# 4. Logical Operators


age = 22
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)


# --------------------------------------------------
# 5. Membership Operators

name = "Bhakti"

print("B" in name)
print("z" in name)
print("z" not in name)


# --------------------------------------------------
# 6. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)