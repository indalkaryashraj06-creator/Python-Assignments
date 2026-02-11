# accessing the elements
dict = {"name": "yash" , "age": 18 , "city" : "pune"}
print(dict["name"])
print(dict["age"])
print(dict["city"])
#updating the dictionary
dict["name"] = "amar"
print(dict)
#removing the element 
del dict["name"]
print(dict)
# addition the element
dict["level"] = "easy"
print(dict)
#merging the dictionaries
dict1 = {"name":"amar" }
dict2 = {"gender":"male"}
print(dict1 | dict2)