list = [10,20,30,40,50]
# accesing the element
print(list[0])
print(list[1])
#slicing the list
print(list[1:4])
print(list[:3])
#addding elements to list
list.append(70)
print(list)
list.insert(3,45)
print(list)
#removing the element
list.remove(45)
print(list)
list.pop()
print(list)
del list[3]
print(list)
# sorting list elements 
list = [20,30,40,10,50]
list.sort()
print(list)
#sorting list elements 
list =[10,20,30,50,40]
sorted(list)