def with_third_variable(a, b):
    print("--Before Swapping--")
    print(f"a is {a}, b is {b}")

    t = a
    a = b
    b = t

    print("--After Swapping--")
    print(f"a is {a}, b is {b}")

def without_third_variable(a, b):
    print("--Before Swapping--")
    print(f"a is {a}, b is {b}")
   
    a = a + b
    b = a - b
    a = a - b # a, b = b, a
    
    print("--After Swapping--")
    print(f"a is {a}, b is {b}")


a = int(input("Enter a:"))
b = int(input("Enter b:"))

with_third_variable(a, b)
without_third_variable(a, b)