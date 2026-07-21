def largest_of_two_n(a, b):
    if a > b:
        print(f"{a} > {b}")
    else:
        print(f"{b} > {a}")

def largest_of_three_n(a, b, c):
    if a > b and a > c:
        print(f"{a} > b and c")
    elif b > a and b > c:
        print(f"{b} > a and c")
    else:
        print(f"{c} > a and b")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

largest_of_two_n(a, b)
largest_of_three_n(a, b, c)
