def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        L = arr[m:]
        R = arr[:m]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1


# arr = [33, 22, 11,50,78, 43]
arr = [10, 5, 2, 11, 1, 6, 9, 0]

print(arr)
merge_sort(arr)
print(arr)
