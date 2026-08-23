def sum_without_recursion(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sum_with_recursion(n):
    if n == 1:
        return 1 
    return n + sum_with_recursion(n - 1)

n = int(input())

s1 = sum_without_recursion(n)
s2 = sum_with_recursion(n)

print(s1)
print(s2)