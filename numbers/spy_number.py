def check_spy(n):
    str_n = str(n)
    sum = 0
    product = 1
    for i in str_n:
        sum += int(i)
        product *= int(i)

    return sum == product

n = int(input("Enter a number:"))
res = check_spy(n)
print(f"{"Spy" if res else "Not Spy"}")