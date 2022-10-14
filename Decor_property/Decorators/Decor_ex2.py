

def decor(addition):
    def inner():
        result = addition() #exiting functionality
        #add new functionality here
        num3 = float(input("Enter third number:"))
        result = result + num3
        return result
    return inner

@decor
def addition():
    num1 = float(input("Enter 1st Number"))
    num2 = float(input("Enter 2nd Number"))
    result = num1 + num2
    return result

#addition = decor(addition)
print("addition is :",addition())