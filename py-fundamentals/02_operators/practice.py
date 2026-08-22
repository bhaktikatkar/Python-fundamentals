# Practice


# 1. Arithmetic Operators
# arthematic operations on two integers

print("enter two values")
x = int(input())
y = int(input())

a = x - y
b = x + y
c= x / y
d = x // y
e = x % y
f = x ** y

print("subtraction is",a)
print("addition is",b)
print("division is",c)
print("floor division is",d)
print("modulud is",e)
print("power is",f)

#------------------------------------------------------------------------------------------------
# 2. Relational Operators
# Compare two numbers using all comparison operators.

x = 15
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#---------------------------------------------------------------------------------------------------
# 3. Logical Operators
# Check whether a person is eligible based on age and whether they have an ID

age = 20
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

#-----------------------------------------------------------------------------------------------------
# 4. Assignment Operators
# Start with a number and update it using
# different assignment operators.

print("enter any number")
number = int(input())

number += 5
print(number)

number -= 2
print(number)

number *= 3
print(number)

number /= 2
print(number)

#----------------------------------------------------------------------------------------------------------
# 5. Simple Real-Life Problem
# 5.1.Calculate the total marks and percentage.

maths = 85
python = 90
robotics = 80

total = maths + python + robotics
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)

#=======================================================
# 5.2.accept ht and wt and calculate area of rectangle

print("enter two values")

h = int(input())
w = int(input())

area = h * w 

print("area of rectangle",area)

#=========================================================
#5.3.whether a number is grater than less than or equal to 10

print("enter any number")
num = int(input())

if (num > 10):
    print("num is grater than 10")
if (num < 10):
    print("num is less than 10")
if (num == 10):
    print("num is equals to 10")




    