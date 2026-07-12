def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    elementSmaller = []
    elementLarger = []
    pivot = arr[n - 1]
    for i in range(n-1):
        if arr[i] < pivot:
            elementSmaller.append(arr[i])
        else:
            elementLarger.append(arr[i])

    return quick_sort(elementSmaller) + [pivot] + quick_sort(elementLarger)

arr = [-5, 0, -10, 15, -2, 8, -50]
sortedArray = quick_sort(arr)
print(sortedArray)