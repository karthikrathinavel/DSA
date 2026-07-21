def prime_check(num):
    if num <= 1:
        return False
        
    for i in range(2, num):
        if num % i == 0:
            return False 

    return True

num = int(input("Enter a number: "))

res = prime_check(num)
print(f"{num} is {'Prime' if res else 'Not a Prime'}")
