def get_factors(num):
    num = abs(num)

    if num == 0:
        return []
    
    factors = []
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            count += 1

    return [factors, count]

num = int(input("Enter a number:"))
res = get_factors(num)

print(f"The factors of {num} are: {res[0]}")
print(f"count: {res[1]}")