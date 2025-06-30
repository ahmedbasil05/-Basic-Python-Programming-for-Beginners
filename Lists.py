#LIST [] - ordered and mutable. Duplicates OK

fruits = ["apple", "banana","peach","mango"]
print(fruits)

student_info = ["xyz", 20, 3.2, True]
print(student_info)
print("cgpa", student_info[2])   #printing cgpa

#slicing - printing the list backward
ages = [23, 54, 67]
print(ages[::-1])

#iterate a list using for loop

char = ["a","b","c"]
for ch in char:
    print(ch)

#LIST METHODS
print(len(char))
print(char.append("d"))
print(char.remove("c"))
print(char.insert(1, "x"))
print(ages.sort())
print(ages.reverse())
print(fruits.clear())


#help() - tells about all the list methods