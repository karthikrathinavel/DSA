def dec_to_bin(n):
    return bin(n).replace("0b", "")

def bin_to_dec(m):
    return int(m, 2)

n = int(input("Enter a number:"))
print(f"The binary representation of {n} is {dec_to_bin(n)}")

m = input("Enter a binary number: ")
print(f"The decimal representation of {m} is {bin_to_dec(m)}")