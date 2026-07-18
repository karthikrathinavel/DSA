def find_max(list):
    min = list[0]
    for i in list:
        if list[i] < min:
            min = list[i]
    return min

def find_min(list):
    max = list[0]
    for i in list:
        if list[i] > max:
            max = list[i]
    return max

list = [23, 45, 12, 112, 65]
min = find_min(list)
max = find_max(list)
print(f"Min element in the {list} is {min}")
print(f"Max element in the {list} is {max}")