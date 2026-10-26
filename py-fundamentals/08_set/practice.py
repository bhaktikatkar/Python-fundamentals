# Day 8 - Sets Practice


#--------------------------------------------------------------------------
# 1. Created a set of 5 programming languages and print it.
languages = {"Python", "C", "C++", "Java", "SQL"}
print(languages)

#-------------------------------------------------------------------------
# 2. Created a set containing duplicate numbers.
# Observe how Python handles duplicates.
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)

#--------------------------------------------------------------------------
# 3. Added "JavaScript" to the languages set.
languages.add("JavaScript")
print(languages)

#--------------------------------------------------------------------------
# 4. Added multiple elements to a set.
languages.update(["HTML", "CSS"])
print(languages)

#---------------------------------------------------------------------------
# 5. Removed an element from a set.
languages.remove("C")
print(languages)

#----------------------------------------------------------------------------
# 6. Used discard() to remove an element that may not exist.
languages.discard("Ruby")
print(languages)

#-----------------------------------------------------------------------------
# 7. Checked whether "Python" exists in the set.
print("Python" in languages)

#--------------------------------------------------------------------------
# 8. Found the number of unique elements.
print("Unique elements:", len(numbers))

#-----------------------------------------------------------------------------
# 9. Found the union of two sets.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a.union(set_b))

#----------------------------------------------------------------------------
# 10. Found the common elements using intersection().
print("Intersection:", set_a.intersection(set_b))

#---------------------------------------------------------------------------
# 11. Found elements present in set_a but not set_b.
print("Difference:", set_a.difference(set_b))

#----------------------------------------------------------------------------
# 12. Found the symmetric difference.
print("Symmetric difference:", set_a.symmetric_difference(set_b))

#-----------------------------------------------------------------------------
# 13. Removed duplicate names from a list.
names = ["Amit", "Priya", "Amit", "Rahul", "Priya"]
unique_names = set(names)
print(unique_names)


