"""
i=1
v=5
x=10
l=50
c=100
"""

n = 9

d = {1: "i", 4:"iv", 5: "v", 9:"ix", 10: "x", 50: "l", 100: "c"}

"""
if n-key==1 , ans=key-1,key

"""

_keys = list(d.keys())
# _keys.reverse()


# if n in d:
#     print(d[n])
# else:
#     for i in range(len(_keys)):
#         if _keys[i]-n == 1:
#             print((n-_keys[i])*d[_keys[0]] + d[_keys[i]])
#             break


l = [100, 50, 10, 5, 1]
# n=13 >10, 13-10=3
n=13
for i in l:
    if n - i > 1:
        k = n % i,  # 3
        c = n / i
        print(str(c) + "" + str(k))
    # else:
    #     print("i"+d[l[i]])
    #



