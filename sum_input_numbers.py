number1 = int(input('¿What is your first number?')) #asks for the first number and converts it to integer (the input function always returns a string)
number2 = int(input('¿What is your second number?')) #read above

result = number1+number2 #sums te two numbers
result = str(result) #converts result to string so it can be printed along text

print('The result of your two numbers is: ' + result) #prints the string and concatenates with the result that also stores a string
