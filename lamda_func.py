def multiply(x,y):
    return x * y
print(multiply(2,40))

#using lambda function
multiply = lambda x, y : x * y
print(multiply(2,40))

#passing lambda function as argument 
def createMultiplier(x):
    return lambda y : x * y
multiply = lambda # type: ignore