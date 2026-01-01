print("  |welcome to calculator app|  ")
num1 = float(input("num1 : "))
num2 = float(input("num2 : "))
print("-------------------------------")
print("Adding :  " + str(num1+num2))
print("Subtract : "+ str(num1-num2))
print("multiply : "+ str(num1*num2))
if num2 != 0:
    print("Division: ", num1 / num2)
    print("Modulus: ",num1 % num2)
else :
    print("division:Error (cannot divide byzero)")
    print("Modulus:Error (cannot divide by zero)")