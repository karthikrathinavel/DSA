def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #temp = arr[i]
        #arr[i] = arr[min_idx]
        #arr[min_idx] = temp
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [12, 34, 21, 15, 11, 56, 100, 76]
sorted_array = selection_sort(arr)
print(sorted_array)