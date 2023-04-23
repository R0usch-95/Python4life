#write a prgramm if number divisible by 3 then it return "fizz" if it is divisible by 5 return "Buzz" if it is divisible by bth return "FizzBuzz"
#number = int(input("enter the number: "))
choice = 'y'

while(choice == 'y' ):
    number = int(input("enter the number: "))
    if(number%3 == 0 and number%5 == 0)
        print("FizzBuzz")
        choice = str(input("do you want to contioue y/n:"))
        continue
    elif(number%3 == 0):
        print("Fizz")
        choice = str(input("do you want to contioue y/n:"))
        continue
    elif(number%5 == 0):
         print("Buzz")
         choice = str(input("do you want to contioue y/n:"))
         continue
    else:
        print("invaid input")
        choice = str(input("do you want to contioue y/n:"))
        continue

