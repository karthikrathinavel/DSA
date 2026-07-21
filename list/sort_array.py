def sort_ascending(arr):
    arr.sort()
    return arr

def sort_descending(arr):
    arr.sort(reverse=True)
    return arr

arr = [23, 45, 12, 112, 65]
print(f"sort ascending: {sort_ascending(arr)}")
print(f"sort descending: {sort_descending(arr)}")