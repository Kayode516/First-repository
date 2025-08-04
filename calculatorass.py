# Calculators
number_1 = int(input("INPUT NUMBER"))
number_2 = int(input("INPUT NUMBER"))
# choose operation
operation = input("CHOOSE OPERATION (+, -, *, /): ")
# Perform calculation based on the operation
if operation == '+':
    result = number_1 + number_2
    print("Result:", result)
elif operation == '-':
    result = number_1 - number_2
    print ("Result:", result)
elif operation == '*':
    result = number_1 * number_2
    print("Result:", result)
elif operation == '/':
    result = number_1 / number_2
    print("Result:", result)
else:
    print("Invalid Input")