def check_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = int(input("Enter a number:"))
r = check_palindrome(num)
print(f"{"Palindrome" if r else "Not a Palindrome"}")