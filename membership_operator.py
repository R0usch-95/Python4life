letter = "apartment"
for ch in letter:
    print(ch)

#find the unique number using membership operator
list = [10 , "key" , ['abc'] , 25, 10, ['abc']]
unique = []
for ch in list:
    if ch not in unique:
        unique.append(ch)
print(unique)