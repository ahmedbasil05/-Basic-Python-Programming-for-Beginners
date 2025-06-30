# EXERCISE

email = input("enter ur email:")
index = email.index("@") #pivot-point

username = email[:index]
domain = email[index:]

print(f"your username is {username} and domain is {domain}")