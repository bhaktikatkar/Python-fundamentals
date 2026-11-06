# Day 9 - Dictionaries Practice


#Create a dictionary containing your personal details.
student = {
    "name": "Bhakti",
    "age": 21,
    "branch": "Robotics and AI",
    "college": "MGM University"
}
print(student)   #{'name': 'Bhakti', 'age': 21, 'branch': 'Robotics and AI', 'college': 'MGM University'}


#Access the student's name and branch.
print(student["name"])  #Bhakti
print(student["branch"]) #21


#Access a value using get().
print(student.get("age")) #{'name': 'Bhakti', 'age': 21, 'branch': 'Robotics and AI', 'college': 'MGM University', 'city': 'Sambhajinagar'}


#Add a new key called "city".
student["city"] = "Sambhajinagar"
print(student)  #{'name': 'Bhakti', 'age': 22, 'branch': 'Robotics and AI', 'college': 'MGM University', 'city': 'Sambhajinagar'}


#Update the student's age.
student["age"] = 22
print(student)  #{'name': 'Bhakti', 'age': 22, 'branch': 'Robotics and AI', 'college': 'MGM University'}


#Remove the city key using pop().
student.pop("city")
print(student)  #{'name': 'Bhakti', 'age': 22, 'branch': 'Robotics and AI', 'college': 'MGM University'}


#Print all dictionary keys.
print(student.keys())  #dict_keys(['name', 'age', 'branch', 'college'])


#Print all dictionary values.
print(student.values())  #dict_values(['Bhakti', 22, 'Robotics and AI', 'MGM University'])


#Print all key-value pairs.
print(student.items())   #dict_values(['Bhakti', 22, 'Robotics and AI', 'MGM University'])


#Check whether "name" exists in the dictionary.
print("name" in student)   #True


#Find the total number of entries.
print(len(student))   #4


#Iterate through the dictionary.
for key, value in student.items():
    print(key, ":", value)    #name : Bhakti
                              #age : 22
                              #branch : Robotics and AI
                              #college : MGM University


#Create a dictionary of 5 subjects and their marks.
marks = {
    "Python": 90,
    "SQL": 85,
    "Machine Learning": 88,
    "Excel": 92,
    "Statistics": 80
}
print(marks)           #{'Python': 90, 'SQL': 85, 'Machine Learning': 88, 'Excel': 92, 'Statistics': 80}


#Calculate the total marks.
print("Total:", sum(marks.values()))  #Total: 435


#Calculate the average marks.
average = sum(marks.values()) / len(marks)
print("Average:", average)         #Average: 87.0


#Find the subject with the highest marks.
highest_subject = max(marks, key=marks.get)
print("Highest scoring subject:", highest_subject)  #Highest scoring subject: Excel


#Create a nested dictionary of three students.
students = {
    "student1": {"name": "Amit", "marks": 85},
    "student2": {"name": "Priya", "marks": 92},
    "student3": {"name": "Rahul", "marks": 78}
}

print(students["student2"]["name"])   #Priya
print(students["student2"]["marks"])  #92


