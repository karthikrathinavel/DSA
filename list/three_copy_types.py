import copy

original = [1, 2, [3, 4]]

# NORMAL COPY
assigned = original 

# Modify the assigned list
assigned[0] = 99
assigned[2][0] = 88

print(f"Normal copy - original list: {original}") 

# SHALLOW COPY
shallow = original.copy()

shallow[0] = 99
shallow[2][0] = 88

print(f"Shallow copy - original list: {original}") 

# DEEP COPY
deep = copy.deepcopy(original)

deep[0] = 99
deep[2][0] = 88

print(f"Deep copy - original list: {original}") 



