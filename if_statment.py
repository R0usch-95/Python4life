def max_num(num1,num2,num3):
    if num1 < num2 & num3 < num2:
        print("second number is greater than other two")
    elif num2 < num1 & num3 < num1:
        print("first number is greater than other two")
    else:
        print("third number is greater than other two")

max_num(55,17,38)