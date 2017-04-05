someValue = 5

def letsAdd(x, y):
    #Addition function
    addition = x + y
    return addition

def subtraction(x, y):
    #Subtraction function
    subtract = x - y
    return subtract

def moreSubtraction(x, y, z):
    return x - y - z

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


print "3 plus 5 is: " + str(letsAdd(3, 5))
print "10 minus 4 is: " + str(subtraction(10, 4))
print "40 minus 3 minus 11 is: " + str(moreSubtraction(40, 3, 11))
print "10 times 5 is: " + str(multiplication(10, 5))
print "50 divided by 5 is: " + str(division(50, 5))


