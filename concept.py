# Python Fundamentals - Day 6
# Topic: Lists

# 1. Creating a List
# --------------------------------------------------

fruits = ["apple", "banana", "mango", "orange"]
print(fruits)


# --------------------------------------------------
# 2. Accessing List Elements

print(fruits[0])     
print(fruits[1])
print(fruits[-1])     


# --------------------------------------------------
# 3. Changing List Elements

fruits[1] = "grapes"
print(fruits)


# --------------------------------------------------
# 4. Adding Elements

fruits.append("watermelon")
print(fruits)


# insert() adds an element at a specific position

fruits.insert(1, "banana")
print(fruits)


# --------------------------------------------------
# 5. Removing Elements

fruits.remove("orange")
print(fruits)


# pop() removes an element using its index
# If no index is given, it removes the last element

fruits.pop()
print(fruits)


# --------------------------------------------------
# 6. Length of a List

print("Length:", len(fruits))


# --------------------------------------------------
# 7. List Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
print(numbers[2:])
print(numbers[:4])


# --------------------------------------------------
# 8. Checking Elements

print(30 in numbers)
print(100 in numbers)


# --------------------------------------------------
# 9. Sorting a List

marks = [75, 92, 68, 88, 81]
marks.sort()
print(marks)


# reverse() reverses the list
marks.reverse()
print(marks)


# --------------------------------------------------
# 10. Useful Functions

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Total:", sum(numbers))