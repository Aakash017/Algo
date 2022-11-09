'''Given a number n, print following a pattern without using any loop.

Examples :

Input: n = 16
Output: 16, 11, 6, 1, -4, 1, 6, 11, 16

Input: n = 10
Output: 10, 5, 0, 5, 10
'''

n=10

s=True
l=[n]
c=0
while s:
    n=n-5
    l.append(n)
    c=c+1
    if n<=0:
        for i in range (c):
            n=n+5
            l.append(n)
        s=False
print(l)
#
# # write your code here
#
import sys


# N = int(input())
#
# def get_sum(n):
#     sum1 = 0
#     while (n != 0):
#         sum1 = sum1 + n % 10
#         n = n // 10
#
#     return sum1
#
#
# def smallestNumber(N):
#     i = 1
#     while (1):
#         if (get_sum(i) == N):
#             print(i)
#             break
#         i += 1
#
#
# smallestNumber(N)


# def Convert(string):
#     list1 = []
#     list1[:0] = string
#     return list1
#
#
# # Driver code
# str1 = "000000000002041"
# new_list = Convert(str1)
# print(new_list)


#
# for i in new_list:
#     if i == "0":
#         new_list.pop(new_list.index(i))
# print(new_list)


# def remove_omitted_zero(l):
#     i = 0
#     n=len(l)
#     while i < n:
#         if l[0] == "0":
#             l.pop(0)
#         i += 1
#
#
# remove_omitted_zero(l=new_list)
# print(new_list)
# new_list.sort(reverse=True)
# print(new_list)
# i =int("".join(new_list))
# print(type(i))





# write your code here



def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

def remove_omitted_zero(l):
    i = 0
    n=len(l)
    while i < n:
        if l[0] == "0":
            l.pop(0)
        i += 1
def find_number_divisble_by_fifteen(i):
    while i>15:
        if i%15==0:
            return i
        else:
            i=i-1
# str1=sys.argv[1]
# new_list = Convert(str1)
# remove_omitted_zero(l=new_list)
# new_list.sort(reverse=True)
# i =int("".join(new_list))
# print(find_number_divisble_by_fifteen(i))

