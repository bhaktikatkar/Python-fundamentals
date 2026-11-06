# Day 9 - Dictionaries

# Creating a dictionary
student = {
    "name": "Bhakti",
    "age": 22,
    "branch": "Robotics and AI"
}

print(student) #{'name': 'Bhakti', 'age': 22, 'branch': 'Robotics and AI'}

#--------------------------------------------------------------------------------------------------
# Accessing values using keys
print(student["name"])  #Bhakti
print(student["age"])    #22

#--------------------------------------------------------------------------------------------------
# Using get()
print(student.get("branch")) #Robotics and AI
print(student.get("city"))   #none

#-----------------------------------------------------------------------------------------------------
# Adding a new key-value pair
student["city"] = "Sambhajinagar" 
print(student)  #none

#---------------------------------------------------------------------------------------------------
# Updating an existing value
student["age"] = 21
print(student)   #{'name': 'Bhakti', 'age': 21, 'branch': 'Robotics and AI', 'city': 'Sambhajinagar'}

#-------------------------------------------------------------------------------------------------------------
# Removing an element using pop()
student.pop("city")
print(student)  #{'name': 'Bhakti', 'age': 21, 'branch': 'Robotics and AI'}

#----------------------------------------------------------------------------------------------------------------
# Getting all keys
print(student.keys())  #dict_keys(['name', 'age', 'branch'])

#---------------------------------------------------------------------------------------------------------------
# Getting all values
print(student.values())  

#---------------------------------------------------------------------------------------------------------------
# Getting all key-value pairs
print(student.items())

#-------------------------------------------------------------------------------------------------------------
# Checking whether a key exists
print("name" in student)

#--------------------------------------------------------------------------------------------------------------
# Finding dictionary length
print(len(student))

#----------------------------------------------------------------------------------------------------------------
# Looping through dictionary keys
for key in student:
    print(key)

#----------------------------------------------------------------------------------------------------------------
# Looping through values
for value in student.values():
    print(value)

#---------------------------------------------------------------------------------------------------------------
# Looping through key-value pairs
for key, value in student.items():
    print(key, ":", value)

#-------------------------------------------------------------------------------------------------------------------
# Nested dictionary
students = {
    "student1": {
        "name": "Amit",
        "marks": 85
    },
    "student2": {
        "name": "Priya",
        "marks": 90
    }
}

print(students["student1"]["name"])
print(students["student2"]["marks"])