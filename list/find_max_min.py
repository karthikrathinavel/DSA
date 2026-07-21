def find_min(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def find_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def second_max(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

def second_min(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[1]

arr = [23, 45, 12, 112, 65]
min = find_min(arr)
max = find_max(arr)
second_max = second_max(arr)
second_min = second_min(arr)
print(f"Min element in the {arr} is {min}")
print(f"Max element in the {arr} is {max}")
print(f"Second Max element in the {arr} is {second_max}")
print(f"Second Min element in the {arr} is {second_min}")