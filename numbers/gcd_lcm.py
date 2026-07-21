import math

def gcd_in(a, b):
    return math.gcd(a, b)

def lcm_in(a, b):
    return math.lcm(a, b)

a = int(input("Enter a:"))
b = int(input("Enter b:"))


print(f"GCD of {a} and {b} is {gcd_in(a, b)}")
print(f"LCM of {a} and {b} is {lcm_in(a, b)}")