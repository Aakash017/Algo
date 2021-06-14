l = [1, 8, 30, 40, 90, 100, 80]
n = 10
s = []


def find(l, n):
    i, j = 0, 1
    while i < len(l) and j < len(l):
        if l[j] - l[i] == n:
            print(l[i], l[j])
            s.append((l[i], l[j]))
            i += 1
            j += 1
        elif l[j] - l[i] < n:
            j += 1
        else:
            i += 1
    return s


print(find(l, n))
