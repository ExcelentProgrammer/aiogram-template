# This function calculates the factorial of a number
def factorial(n):
    # If the input is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Otherwise, recursively calculate the factorial
        return n * factorial(n-1)
