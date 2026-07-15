n = int(input("Enter a number"))

#Iterative method
def factorial_iterative(num):
    iter_factorial = 1
    for i in range(1, num + 1):
        iter_factorial *= i
    return iter_factorial

#Recursive method
def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)

if n < 0:
    print("Error: Negative numbers have no factorials.")
else:
    iterOut = factorial_iterative(n)
    recursOut = factorial_recursive(n)
    print(f"Iterative method out: {iterOut}")
    print(f"Recursive method out: {recursOut}")
