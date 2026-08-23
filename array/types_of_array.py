# Fixed size array
a = [0] * 5
print(a)
for i in range(5):
    a[i] = i + 1
print(a)

# dynamic sized array
arr = []
arr.append(10)
arr.append(20)
arr.append(30)
print(arr)
arr.pop()
print(arr)

# One-dimensional array
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(b)):
    print(f"a[{i}]={i}", end = " ")

# Two-dimensional array
c = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
for i in range(len(c)):
    for j in c[i]:
        print(f"c[{i}][{j}] = {j}", end = " ")

# Three-dimensional array
d = [[[1, 2, 3], [7, 8, 9]], [[4, 5, 6], [10, 11, 12]]]
for i in range(len(d)):
    for j in d[i]:
        for k in j:
            print(f"d[{i}][{j}][{k}] = {k}", end = " ")