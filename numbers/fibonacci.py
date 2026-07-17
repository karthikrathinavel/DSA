# Iterative Method
def fibonacci_iterative(n):
    fib_list = [0, 1]
    for i in range(2, n):
        el = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(el)
    return fib_list[:n]

# Recursive Method
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
terms = int(input("Enter number of terms:"))
if terms <= 0:
    print("Error: Please enter a positive integer")
else:
    iter_series = fibonacci_iterative(terms)
    print(f"Iterative series: {iter_series}")
    recurs_series = [fibonacci_recursive(i) for i in range(terms)]
    print(f"Recursive series: {recurs_series}")
