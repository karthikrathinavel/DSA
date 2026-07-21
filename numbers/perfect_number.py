def check_perfect(n):
    div = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    for j in div:
        sum += j

    return sum == n


n = int(input("Enter a number"))
res = check_perfect(n)
print(f"{"Perfect" if res else "Not a perfect"}")