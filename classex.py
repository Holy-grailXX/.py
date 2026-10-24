def factorial (n):
    result = 0 
    if n == 0 or n == 1:
        return 1
    else :
        result = n*factorial (n-1)
        return result
number = int (input("Enter a number to find the factorial "))
print("The factorial of ",number,"is", factorial(number))
