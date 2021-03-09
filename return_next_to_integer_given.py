value1 = int(input("what is your number?: ")) #asks for the first value
value2 = 1  #saves 1 in the second value

def operation(value1, value2): #defines the operation function and sets value1 and value2 as parameters
    result = value1 + value2 #sets the result to be the sum of values 1 and 2
    return result       #tells the function to return result as the result of the function

print(operation(value1,value2))     #prints the result of the operation with the values given
