def reverse_a_number_slicing(num):
    sign = -1 if num < 0 else 1
    n = str(abs(num))[::-1]
    return int(n) * sign

def reverse_math(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = (reverse * 10) + digit
        num = num // 10
    return reverse * sign

num = int(input("Enter a number"))
slice_reverse = reverse_a_number_slicing(num)
math_reverse = reverse_math(num)
print(f"slice_reverse: {slice_reverse}")
print(f"math_reverse: {math_reverse}")
