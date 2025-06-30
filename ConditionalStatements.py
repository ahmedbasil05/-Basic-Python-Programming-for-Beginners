#CONDITIONAL STATEMENTS

# if
age = int(input("enter ur age:"))

if age > 18:
    print("Elgible to castevote")

# if-else   
marks = int(input("Enter the marks:"))

if marks > 50 : 
    print("Exams passed!")

else:
    print("Retake the exmas")  

# if-elif
age = int(input("Enetr the age:"))   

if age < 20 :
    print("Teenage boy")
elif age > 20 and age < 50 : 
    print("Young Citizen")   
else:
    print("Senior Citizen)")     