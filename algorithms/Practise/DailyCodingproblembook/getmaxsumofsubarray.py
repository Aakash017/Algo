"""
find maximum sum of array using kdans algo

"""


def findmaxarraysum(arr):
    curr_sum = arr[0]
    global_sum = arr[0]
    for i in range(len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        if curr_sum > global_sum:
            global_sum = curr_sum
    print(global_sum)


findmaxarraysum([-3, -4, 5, -1, 2, -4, 6, -1])
findmaxarraysum([-2, 3, -1, 2])
