def check_neon(n):
    sq = n ** 2
    str_n = str(sq)
    total = 0
    for i in str_n:
        total += int(i)

    return total == n
    

n = int(input("Enter a number:"))
res = check_neon(n)
print(f"{"Neon" if res else "Not a neon"}")