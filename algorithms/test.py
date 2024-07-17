# # # 1-10
# #
# #
# # def r(n):
# #     print(n)
# #     n=n+1
# #     if n<11:
# #         r(n)
# #     return True
# # print(r(1))
# #
# # # Find missing element
# # n = 5
# # l = [2,5,1,3]
# # sum=0
# # for i in range(1,len(l)):
# #     sum+=i
# #
# # sum=15
# # l=[11]
# #
# #
# #
# # 'select count(employees) from employee where dept_id=1'
# # 'select max(salary) from employee table where dept_id=1'
# # 'select distinct salary from employee order by salary desc limit 3 , 1'
# #
# #
"""GitHUb Hack"""

import os
from random import randint
for i in range(300, 400):
    for j in range(1, randint(0, 3)):
        d = str(i)+"days ago"
        with open("file.txt", 'a') as f:
            f.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')
os.system('git push origin master')

# l = [1, 9, 5, 3, 8, 23, 10]
#
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)
#
# _l, _r = 0, len(l) - 1
# while _l < _r:
#     m = (_l + _r) // 2
#     if l[m] == 10:
#         print("index = ", m)
#         _l += 1
#         _r -= 1
#     elif l[m] > 10:
#         _r = m - 1
#     else:
#         _l = m + 1
#
# a = (0 + 5) / 2
# print("a", a)


s = "{({[}{{{[[))("

l=[]

"""
for loop-

if i ="{" or i="["
add it into list

elif i="}",],)
last elemetn in l= l[-1]=="{" and i="}", l.pop()



"""

