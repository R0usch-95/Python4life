"""dict = {}
name = input("enter the name : ")
mark= input("enter the score here: ")
name = dict.keys()
mark = dict.values()
print(dict.items())"""

sal = {'harry':15, 'mark':13, 'andy':16}

sal['harry']=18
print(sal)
del sal['mark']
print(sal)
for index in sal.keys():
    print(index)

for index in sal.values():
    print(index)

for key,val in sal.items():
    print(key, val)
print('andy' in sal)
