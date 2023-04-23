# # 1-10
#
#
# def r(n):
#     print(n)
#     n=n+1
#     if n<11:
#         r(n)
#     return True
# print(r(1))
#
# # Find missing element
# n = 5
# l = [2,5,1,3]
# sum=0
# for i in range(1,len(l)):
#     sum+=i
#
# sum=15
# l=[11]
#
#
#
# 'select count(employees) from employee where dept_id=1'
# 'select max(salary) from employee table where dept_id=1'
# 'select distinct salary from employee order by salary desc limit 3 , 1'
#
#
"""GitHUb Hack"""

import os
from random import randint
for i in range(1, 15):
    for j in range(1, randint(0, 10)):
        d = str(i)+"days ago"
        with open("file.txt", 'a') as f:
            f.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')
os.system('git push origin master')

