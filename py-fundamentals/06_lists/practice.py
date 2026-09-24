# Day 6 - Lists Practice

# 1. Create a list of 5 subjects you are studying.
subjects = ["Python", "SQL", "Machine Learning", "Cloud Computing", "Deep Learning"]
print(subjects)

#-------------------------------------------------------------------------------------
# 2. Print the first and last subject.
print(subjects[0])
print(subjects[-1])

#----------------------------------------------------------------------------------------
# 3. Add "Power BI" to the list.
subjects.append("Power BI")
print(subjects)

#----------------------------------------------------------------------------------------
# 4. Insert "Excel" at the second position.
subjects.insert(1, "Excel")
print(subjects)

#-----------------------------------------------------------------------------------------
# 5. Remove "Cloud Computing" from the list.
subjects.remove("Cloud Computing")
print(subjects)

#------------------------------------------------------------------------------------------
# 6. Create a list of 5 numbers and find their sum.
numbers = [10, 20, 30, 40, 50]
print("Sum:", sum(numbers))

#-------------------------------------------------------------------------------------------
# 7. Find the largest and smallest number.
print("Largest:", max(numbers))
print("Smallest:", min(numbers))

#-------------------------------------------------------------------------------------------
# 8. Print the first three elements using slicing.
print(numbers[:3])

#-----------------------------------------------------------------------------------------------
# 9. Check whether 30 exists in the list.
print(30 in numbers)

#------------------------------------------------------------------------------------------
# 10. Create a list of marks and calculate the average.
marks = [85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print("Average:", average)

#-----------------------------------------------------------------------------------------------
# 11. Sort the numbers in ascending order.
numbers.sort()
print(numbers)

#------------------------------------------------------------------------------------------------
# 12. Reverse the list.
numbers.reverse()
print(numbers)

#---------------------------------------------------------------------------------------------------
# 13. Create a list of fruits and print each fruit using a for loop.
fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

#---------------------------------------------------------------------------------------------------
# 14. Create a list of numbers and print only the even numbers.
values = [12, 7, 18, 5, 20, 9, 14]

for value in values:
    if value % 2 == 0:
        print(value)


