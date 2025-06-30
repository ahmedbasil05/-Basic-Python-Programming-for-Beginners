#STRING METHODS

name = input("enetr your name")
sec_name = "bro"

print(len(name))  #length of the name
print(name.upper) #uppercase
print(name.lower) #lowercase
print(name.find(""))  #first occurence of string
print(name.rfind("")) #last occurence of string
print(name + sec_name) #concatenation
print(name.isdigit()) #returns true if string contains all integer numbers
print(name.isalpha()) #returns true if string has all alphabets

print(name.replace("h","A"))