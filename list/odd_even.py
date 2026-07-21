def even_odd_count_withSeperate(arr):
    e_count = 0
    o_count = 0
    e = []
    o = []
    for i in arr:
        if i % 2 == 0:
            e_count += 1
            e.append(i)
        else:
            o_count += 1
            o.append(i)
    return [e_count, o_count, e, o]


arr = [23, 45, 12, 112, 65]
c_res = even_odd_count_withSeperate(arr)
print(f"Number of even: {c_res[0]}, Number of odd: {c_res[1]}")
print(f"Even list: {c_res[2]}, Odd list: {c_res[3]}")