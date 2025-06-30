#WHILE LOOP - execute some code while some condition remains true

#EXAMPLE 01
name = input("Enter your name:")
while name == "":
    print("You did not enter any name")
    name = input("Enter your name:")

print(f"your name is {name}")    

#EXAMPLE 02
num = int(input("Enetr a number between 1-10:"))
while num < 1 or num > 10:
    print("inavlid number")
    num = int(input("Enetr a number between 1-10:"))

print(f"The number entered is {num}")




