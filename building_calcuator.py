operation=str(input("enter the operation : "))
num1=float(input("enter the first number :"))
num2=float(input("enter the second number :"))

if(operation == "+") | (operation == "add"):
    result = num1 + num2
    print("the addition of two number is ",result)

elif(operation == "-") | (operation == "sub"):
    result = num1 - num2
    print("the subtraction of two number is ",result)

elif(operation == "*") | (operation == "mult"):
    result = num1 * num2
    print("the multiplication of two number is ",result)

elif( operation == "/") | ( operation == "div"):
    result = num1 / num2
    print("the addition of two number is ",result)

elif(operation == "%") | (operation == "mod"):
    result = num1 % num2
    print("the modulous of two number is ", result)

else:
    print("do you want to continue")
