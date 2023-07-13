def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

# Test the factorial function
number = 5
factorial_result = factorial(number)
print(f"The factorial of {number} is: {factorial_result}")