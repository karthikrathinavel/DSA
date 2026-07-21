def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def check_strong(n):
    if n < 0:
        return False
    str_n = str(n)
    str_len = len(str_n)
    total = 0
    for i in str_n:
        total += factorial(int(i))

    return total == n

n = int(input("Enter a number"))
res = check_strong(n)
print(f"{"Strong" if res else "Not strong"}")