# deletion - from beginning
arr = [10, 20, 30, 40, 50]
print("Array before deletion")
for i in range(len(arr)):
    print(arr[i], end=" ")
del arr[0]
print("Array after deletion")
for i in range(len(arr)):
    print(arr[i], end=" ")

print()

# deletion - from a given position
arr = [10, 20, 30, 40, 50]
pos = 2
del arr[pos - 1]
for num in arr:
    print(num, end=" ")

print()

# deletion - first occurence
arr = [10, 20, 30, 40, 50]
element = 20
if element in arr:
    arr.remove(element)
for num in arr:
    print(num, end = " ")

print()

# deletion - all occurences
def remove_element(arr, element):
    k = 0
    for i in range(len(arr)):
        if arr[i] != element:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
    return k
arr = [10, 20, 30, 40, 20, 50]
element = 20
print(remove_element(arr, element))