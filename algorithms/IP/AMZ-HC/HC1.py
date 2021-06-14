#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def quicksort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    l = quicksort([x for x in lst[1:] if x < pivot])
    u = quicksort([x for x in lst[1:] if x >= pivot])
    return l + [pivot] + u


def minimalHeaviestSetA(arr):
    l1 = sorted(arr)
    print(l1)
    l2 = []
    for _ in l1:
        print("_")
        if sum(l1) > sum(l2):
            l2.append(l1.pop())
    print(l2)


if __name__ == '__main__':
    minimalHeaviestSetA([3, 7, 5,6, 2])
    # l2=[]
    # l1=[2,4,5]
    # if sum(l1)>sum(l2):
    #     print("yes")
    # l3=[3,5,6,6,2]
    # print(sorted(l3))

