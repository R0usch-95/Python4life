"""list = []
for index in range(0,10):
    list.append(index)
    #print(list)
print(list)"""

#another method
list = [index for index in range(0,10)]
print(list)
tup = tuple(index for index in range(0,10))
print(tup)
set = {index for index in range(0,10)}
print(set)
dict = {index: index*index for index in range(0,10)}#key=index ,value=index*index
print(dict)