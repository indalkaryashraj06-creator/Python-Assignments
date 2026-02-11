set  = [1,2,3,4,5]
print(set)
set.append(6)
print(set)
set.remove(6)
print(set)
print(2 in set)
print(7 in set)
# operations on set
# union
A = {1,2,3,4}
B = {5,6,7,8}
print(A|B)
#intersection of set 
A = {2,3,4,5}
B = {5,6,7,8}
print(A & B)
# difference of set
A = {2,3,4,5}
B = {4,5,6,7}
print(A-B)
# syymetric difference
A = {2,3,4,5}
B ={ 4,5,6,7}
print(A^B)