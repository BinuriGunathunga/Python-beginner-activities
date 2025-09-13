def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"
 
print("Addition:", calculator(10, 5, "add"))
print("Subtraction:", calculator(10, 5, "subtract"))
print("Multiplication:", calculator(10, 5, "multiply"))
print("Division:", calculator(10, 5, "divide"))
