#DICTIONARIES {:} - a collection of (key:value) pairs
#            ordered and changeable. No duplicates

capitals = {"Pakistan":"Islamabad",
            "India":"New delhi",
            "China":"Beijing"}

print(capitals.get("Pakistan")) #get a vlaue

capitals.update({"germany":"Berlin"}) #insert a vlaue or update
print(capitals)

capitals.pop("China")  #removes a key 
print(capitals)

capitals.popitem()  #removes the latest key:value pair
print(capitals)

capitals.clear()  #removes a dictionary
print(capitals)