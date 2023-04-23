number = [2, 5, 8, 4, 4, 9, 0, 5]
unique = []
for index in number:
    if index not in unique:
        unique.append(index)
        print(unique)
