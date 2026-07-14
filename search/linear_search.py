def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

arr = [3, 4, 5, 2, 1, 7, 8, 6, 10, 9]
target = 7
index = linear_search(arr, target)
print(f"{target} is in index {index}")