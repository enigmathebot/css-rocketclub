nput1 = float(input("Enter the first number"))
operator = input("Please select an operation")
input2 = float(input("Enter the second number"))

if (operator == "x"):
    answer = input1*input2
elif (operator == "/"):
    answer = input1/input2
elif(operator == "+"):
    answer = input1 + input2
else:
    answer = input1 - input2


print("The answer was", answer)