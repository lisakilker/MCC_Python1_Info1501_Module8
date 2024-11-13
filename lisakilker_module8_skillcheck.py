#Program that takes 2 arguments and adds them together and prints the results

def main():
    num1 = 5
    num2 = 20
    
    #Calls sumAndPrint function
    sumAndPrint(num1, num2)
    
    #Calls sumAndReturn function
    result = sumAndReturn(num1, num2)
    print(f"The result returned by (sumAndReturn) is: {result}")

#Adds the two numbers together and prints the result
def sumAndPrint(num1, num2):
    result = num1 + num2
    print(f"The result returned by (sumAndPrint) is: {result}")

#Adds the numbers together and retuns and prints the result
def sumAndReturn(num1, num2):
    result = num1 + num2
    return result

#Calls the main function
if __name__ == "__main__":
    main()