# 1. Linear traversal
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i, end = " ")
# Time complexity: O(n)

print()

# 2. Reverse traversal
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end = " ")
# Time complexity: O(n)

print()

########
# Methods of Array traversal
########
# 1. Using for loop
arr = [10, 20, 30, 40, 50]
for i in arr:
    print(i, end = " ")
# Time complexity: O(n)

print()

#2. Using while loop
arr = [10, 20, 30, 40, 50]
n = len(arr)
i = 0
while i < n:
    print(arr[i], end = " ")
    i += 1
# Time complexity: O(n)

print()

########
# Applications of array traversal
########
# 1. Searching elements
arr = [10, 20, 30, 40, 50]
target = 30
found = False
for i in range(len(arr)):
    if arr[i] == target:
        found = True
        break
if found:
    print("Element found")
else:
    print("Element not found")
# Time complexity: O(n)

print()

# 2. Modify elements
arr = [10, 20, 30, 40, 50]
for i in range(len(arr)):
    arr[i] += 5
for n in arr:
    print(n, end = ' ')
# Time complexity: O(n)

print()