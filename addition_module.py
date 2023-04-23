#write the prgrame 4 multiple choice add,square,expo,exit

first_no = int(input("enter the first number: "))
second_no = int(input("enter the second number: "))
choice = int(input("1:addition \n 2:square \n 3:exponent \n 4:exit \n"))
while(choice <= 3):
    if(choice == 1):
        print("addition is : ",first_no+second_no)
        choice = int(input("1:addition \n 2:square \n 3:exponent \n 4:exit \n"))

    elif(choice == 2):    
        print("square is: ",first_no**2)
        choice = int(input("1:addition \n 2:square \n 3:exponent \n 4:exit \n"))

    elif(choice == 3):   
        print("exponent is : ",first_no**second_no)
        choice = int(input("1:addition \n 2:square \n 3:exponent \n 4:exit \n"))

    else:
        exit