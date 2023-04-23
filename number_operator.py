#Take the number and print the sum of till that number
choice = int(input("1.addition \n2.prime \n3.odd \n4.even \n5.fibinnic \n6.exit \n"))
number = int(input("enter the number: "))
sum = 0
while(choice <= 6):
    for num in range(1,number+1):
        if(choice == 1):
            sum =sum+1
            print(sum)
            