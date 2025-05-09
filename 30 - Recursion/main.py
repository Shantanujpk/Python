# What is recursion function?
# When a function calls itself inside the same function, it's called a recursive function

# Example: Factorial
# 6! = 6*5*4*3*2*1 which is n * (n-1)!

def recursive_function_factorial(n):
    # Base Case: if n is 0 or 1, return 1 (since 0! = 1! = 1)
    if (n == 0 or n == 1):
        return 1
    else:
        # Recursive Case: n * factorial of (n - 1)
        return n * recursive_function_factorial(n - 1)

# Calling function:
print(recursive_function_factorial(4))  
# Here's what happens step-by-step:
# recursive_function_factorial(4)
# => 4 * recursive_function_factorial(3)
# => 4 * (3 * recursive_function_factorial(2))
# => 4 * (3 * (2 * recursive_function_factorial(1)))
# => 4 * (3 * (2 * 1)) = 24


# What to do for Fibonacci series?

# Fibonacci definition:
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)

def recursive_function_febSeries(n):
    # Base Case 1: if n is 0, return 0
    if (n == 0):
        return 0
    # Base Case 2: if n is 1, return 1
    elif (n == 1):
        return 1
    else:
        # Recursive Case: f(n-1) + f(n-2)
        return recursive_function_febSeries(n - 1) + recursive_function_febSeries(n - 2)

print(recursive_function_febSeries(5))  
# Here's what happens:
# f(5) = f(4) + f(3)
#      = (f(3) + f(2)) + (f(2) + f(1))
#      = ((f(2) + f(1)) + (f(1) + f(0))) + ((f(1) + f(0)) + 1)
#      = Eventually breaks down to multiple f(1) and f(0) calls, then added up
# Final output: 5

# If you run print(recursive_function_febSeries(15))
# It will take time because it repeats many same calls (e.g., f(3), f(2) again and again)
# So for bigger values, we should use memoization or iteration
