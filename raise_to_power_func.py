def raise_to_power(base_num, pow_num):

    """numb = int(input("enter the number: "))
    power = int(input("enter the power: "))
    result = numb ** power
    print(f"the exponenetial of number {numb} is {result}")"""
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))



