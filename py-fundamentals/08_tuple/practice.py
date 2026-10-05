# Day 7 - Tuples Practice


# Create a tuple containing 5 programming languages.
languages = ("Python", "C", "C++", "Java", "SQL")
print(languages)


# Print the first and last element.
print(languages[0])
print(languages[-1])


# Print the first three elements.
print(languages[:3])


# Find the length of the tuple.
print("Length:", len(languages))


# Check whether "Python" exists in the tuple.
print("Python" in languages)


# Create a tuple of 5 numbers and find their sum.
numbers = (10, 20, 30, 40, 50)
print("Sum:", sum(numbers))


# Find the largest and smallest number.
print("Largest:", max(numbers))
print("Smallest:", min(numbers))


# Create a tuple containing repeated values.
values = (10, 20, 10, 30, 10, 40)


# Print every element using a for loop.
for value in numbers:
    print(value)


# Create a tuple containing your name, age and branch.
student = ("Bhakti", 22, "Robotics & AI")

# Create a tuple of marks and calculate the average.
marks = (85, 90, 78, 92, 88)

average = sum(marks) / len(marks)
print("Average:", average)


#  Create a tuple of numbers and print only even numbers.
numbers2 = (12, 7, 18, 5, 20, 9, 14)

for number in numbers2:
    if number % 2 == 0:
        print(number)


# Create a nested tuple containing 3 students.
students = (
    ("A", 20),
    ("B", 21),
    ("C", 22)
)

print(students[0])
print(students[1][0])
