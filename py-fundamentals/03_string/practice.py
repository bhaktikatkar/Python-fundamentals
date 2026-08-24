# Practice


# 1. Create a string containing full name.
# Print the name and its length.

name = "Bhakti Katkar"

print("Name:", name)
print("Length:", len(name))


# 2. Create a string and print first & last char:

language = "Python"

print("First character:", language[0])
print("Last character:", language[-1])


# 3. Create a string and practice slicing.

text = "Programming"

print(text[0:6])
print(text[3:])
print(text[:5])


# 4. Convert a string into - uppercase,lowercase,title case:

sentence = "python is interesting"

print(sentence.upper())
print(sentence.lower())
print(sentence.title())


# 5. Remove extra spaces from a string.

message = "   I am learning Python   "
print(message.strip())


# 6. Replace a word in a string.

sentence = "I am learning Java"
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)


# 7. Find a word inside a string.

sentence = "Python is useful for Data Science"
print(sentence.find("Data"))
print(sentence.find("Java"))


# 8. Check whether a word exists in a string.

sentence = "I am learning Python"
print("Python" in sentence)
print("Java" in sentence)


# 9. Join two strings together.

first_name = "Bhakti"
last_name = "Katkar"

full_name = first_name + " " + last_name
print(full_name)


# 10. Use an f-string.

name = "Bhakti"
course = "Robotics and AI"

print(f"My name is {name} and I am studying {course}.")


