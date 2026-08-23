# Insert element at the beginning - using in-built method
arr = [10, 20, 30, 40, 50]
element = 50
print("Array before insertion")
for i in range(len(arr)):
    print(arr[i], end = " ")
arr.insert(0, element)
print("\nArray after insertion")
for i in range(len(arr)):
    print(arr[i], end = " ")
# Time complexity: O(n)

print()

# Insert element at the beginning - using custom method
arr = [10, 20, 30, 40, 50]
n = 4
element = 50
print("Array before insertion")
for i in range(len(arr)):
    print(arr[i], end = " ")
for i in range(n-1, -1, -1):
    arr[i+1] = arr[i]
arr[0] = element
print(arr)

# Insert element at a given position - using in-built method
arr = [10, 20, 30, 40, 50]
element = 50
pos = 2
print("Array before insertion")
print(arr)
arr.insert(pos-1, element)
print("Array after insertion")
print(arr)

# Insert at last
arr = [10, 20, 30, 40, 50]
element = 80
print("Array before insertion")
for i in range(len(arr)):
    print(arr[i], end=" ")
arr.append(element)
print("Array after insertion")
for i in range(len(arr)):
    print(arr[i], end=" ")
