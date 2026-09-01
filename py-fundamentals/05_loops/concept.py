# Python Fundamentals - Day 5
# Topic: Loops


# 1. for Loop

for i in range(5):
    print(i)


# --------------------------------------------------
# 2. for Loop with a List

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 3. range() Function

for i in range(1, 6):
    print(i)


# range(start, stop, step)

for i in range(2, 11, 2):
    print(i)


# --------------------------------------------------
# 4. while Loop

count = 1

while count <= 5:
    print(count)
    count += 1


# --------------------------------------------------
# 5. break Statement

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# --------------------------------------------------
# 6. continue Statement

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# --------------------------------------------------
# 7. Nested Loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# --------------------------------------------------
# 8. Loop with Conditional Statement

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")