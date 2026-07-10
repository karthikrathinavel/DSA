def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # binary search only works for sorted list/array
target = 7
index = binary_search(array, target)
print(f"Index of {target} is {index}")