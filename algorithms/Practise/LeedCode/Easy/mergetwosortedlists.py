"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


# def mergeTwoLists(list1, list2):
#     final = []
#     n = len(list1)
#     m = len(list2)
#     if n == 1 and m==0:
#         return list1
#     elif m == 1 and n==0:
#         return list2
#     l = 0
#     r = 0
#     while l < n and r < m:
#         if list1[l] < list2[r]:
#             final.append(list1[l])
#             l += 1
#         elif list1[l] > list2[r]:
#             final.append(list2[r])
#             r += 1
#         elif list1[l] == list2[r]:
#             final.append(list2[r])
#             final.append(list1[l])
#             r += 1
#             l += 1
#     while list1:
#         x=list1.pop(0)
#         if x not in final:
#             final.append(x)
#     while list2:
#         x = list2.pop(0)
#         if x not in final:
#             final.append(x)
#
#     return final
#
#     # fl = n if n < m else m
#     # for i in range(len(list1)):
#     #     for j in range(i+1, len(list2)):
#     #         if list1[i] < list2[j]:
#     #             final.append(list1[i])
#     #         elif list1[i] > list2[j]:
#     #             final.append(list2[j])
#     #         elif list1[i] == list2[j]:
#     #             final.append(list1[i])
#     #             final.append(list2[j])
#     # print(final)


# print(mergeTwoLists([1,2,3,4], [1,3,5,10,11]))
