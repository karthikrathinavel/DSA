n = int(input("Enter a number:"))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

num = int(input("Enter count: "))

def list_numbers(str, num):
    if(str == "even"):
        for i in range(0, num+1):
            if i % 2 == 0:
                print(i, end=" ")
        print("\n")
    elif(str == 'odd'):
        for i in range(0, num+1):
            if i % 2 != 0:
                print(i, end=" ")
        print("\n")
list_numbers("even", num)
list_numbers("odd", num)
            