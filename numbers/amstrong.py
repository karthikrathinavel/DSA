def check_amstrong(n):
    if n < 0:
        return False
    str_n = str(n)
    count = len(str_n)
    total = 0
    for i in str_n:
        total += int(i) ** count

    return int(total) == n

n = int(input("Enter a number"))
res = check_amstrong(n)
print(f"{"Amstrong" if res else "NOT an Amstrong"}")