#NESTED LOOP - a loop within another loop
#            outer loop:
#                 inner loop:

#example 01:
for x in range(2):
    for y in range(1, 11):
        print(y, end="")

#example 02:
rows = int(input("enetr a number:"))
columns = int(input("enetr a number:"))  
symbol = input("enter a symbol:")      

for x in range(rows):
    for y in range(columns):
        print(symbol)