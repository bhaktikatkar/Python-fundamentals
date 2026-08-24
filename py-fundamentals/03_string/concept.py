# Python Fundamentals - Day 3
# Topic: Strings
# single quotes (' ') or double quotes (" ").


# 1. Creating Strings

name = "Bhakti"
course = 'Robotics and AI'

print(name)
print(course)


# --------------------------------------------------
# 2. String Indexing


text = "Python"

print(text[0])   # First character
print(text[1])
print(text[-1])  # Last character


# --------------------------------------------------
# 3. String Slicing


text = "Python"

print(text[0:3])
print(text[2:6])
print(text[:4])
print(text[2:])


# --------------------------------------------------
# 4. String Length

name = "Bhakti"
print(len(name))


# --------------------------------------------------
# 5. Changing Case

text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.title())


# --------------------------------------------------
# 6. Removing Extra Spaces

text = "   Python   "
print(text.strip())


# --------------------------------------------------
# 7. Replacing Characters or Words

text = "I like Java"
print(text.replace("Java", "Python"))


# --------------------------------------------------
# 8. Finding Text

text = "Python Programming"

print(text.find("Python"))
print(text.find("Java"))


# --------------------------------------------------
# 9. Checking a String

text = "Python"

print("Python" in text)
print("Java" in text)


# --------------------------------------------------
# 10. String Concatenation

first_name = "Bhakti"
last_name = "Katkar"

full_name = first_name + " " + last_name
print(full_name)


# --------------------------------------------------
# 11. String Formatting

name = "Bhakti"
age = 22

print(f"My name is {name} and I am {age} years old.")