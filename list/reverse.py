def reverse_array_copy(arr):
    return arr[::-1] # returns new array

def reverse_array_without_copy(arr):
    arr.reverse()
    return arr

arr = [1, 2, 3, 4, 5]
res_copy = reverse_array_copy(arr)
res_n_copy = reverse_array_without_copy(arr)
print(f"Reversed array (copy): {res_copy}")
print(f"Reversed array (without copy): {res_n_copy}")