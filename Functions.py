#FUNCTIONS - a block of reusable code
#           place () after the function name to invoke it

#example 01
def happy_birthday(name, age):     #parameters - order matters
    print(f"birthday boy!{name}")
    print(f"You are {age} years old!")
    print("birthday boy!")
happy_birthday("bro", 20)   #arguments - order matters
happy_birthday("broski", 43)

#example 02
def invoice(username, amount, date):
    print(f"Hello {username}")
    print(f"The {amount}$ is due of: {date}")
invoice("Bro",50, "23 may")
