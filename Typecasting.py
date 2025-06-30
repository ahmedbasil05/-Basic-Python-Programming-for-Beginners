# TYPECASTING - the process of converting values from one datatype to another datatype

name = "bro"
age = 19
cgpa = 3.2
student = True

#type()
print(type(name))

#Explicit Typecasting
age = float(age)
print(f"Now the age is {age}")

cgpa = int(cgpa)
print(f"Now gpa is {cgpa}")

#Implicit Typecasting
x =4
y = 5.2

print(x*y)