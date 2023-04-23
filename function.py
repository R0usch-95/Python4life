def msg():
    name=input("enter the name: ")
    time=float(input("enter the timing in am or pm : "))
    if time < 12:
        print(f"hi,{name},good morning")
    elif (time < 16) & (time > 12):
        print(f"hi {name},good afternoon")
    else:
        print(f"hi {name},good evening")
msg()

"""
def maxi(a, b):
    if a < b:
        return b
    else:
        return a


a = 8
b = 4
print(maxi(a, b))



"""