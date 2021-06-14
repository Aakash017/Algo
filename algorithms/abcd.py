a = [1, 4, 0, 6, 0, 2, 0]
for j in range(len(a)):
    for i in range(j, len(a) - 1):
        if a[j] == 0 and a[i] != 0:
            a[j], a[i] = a[i], a[j]

print(a)
