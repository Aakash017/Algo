def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def findMedianSortedArrays(nums1, nums2):
    target = nums1 + nums2
    target = bubble_sort(target)
    n = len(target)
    if n % 2 != 0:
        m = n // 2
        median = target[m]
    else:
        m = (n + 1) // 2
        median = (target[m] + target[m - 1]) / 2
    return median


print(findMedianSortedArrays([1, 2], [3, 4]))
print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 3], [4, 5]))
print(findMedianSortedArrays([0, 0], [0, 1]))
print(findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4]))
