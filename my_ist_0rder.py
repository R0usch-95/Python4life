
choice = int(input("1.printMember \n2.addMember \n3.insertmoreMember \n4.removeMember \n5.Deletelastmember \n6.Display \n"))
while(choice == "y"):
    Member = [ name for name in input("enter the member name: ").split()]
print(Member, sep=" ")
if(choice == 1 ):
    Member.append("Rose")
    print(Member)
else:
    exit

Member.insert(["David","Bret","Sanju"])
Member.remove(3)
Member.pop()
print(Member[3:5])
