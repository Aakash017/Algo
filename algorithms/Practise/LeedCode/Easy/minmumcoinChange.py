"""
Given an amount and the denominations of coins available, determine how many ways change can be made for amount.
There is a limitless supply of each coin type.

l=[1,4,5] n=8
o={4,4,1}

find no of coins for each element till n

l = [inf,inf,inf,inf,inf,inf,inf,inf]
[0,1,2,3,4,5,6,7]
[0,1,]

for i in range(len(l)):
for c in coins:
    if i%c==0
        l[i]=1
    else:
        l[i]=l[i-1]+i
"""
# n = 6
# coins = [1, 4]
#
# l = [float('inf') for _ in range(n + 1)]
# l[0] = 0
# for i in range(1, len(l)):
#     for c in coins:
#         if i - c >= 0:
#             l[i] = min(l[i], l[i - c] + 1)
# print(l)


def coinChange(self, coins, amount) -> int:
    l = [float('inf') for _ in range(amount + 1)]
    l[0] = 0
    for i in range(len(l)):
        for c in coins:
            if i - c >= 0:
                l[i] = min(l[i], l[i - c] + 1)

    return l[-1] if l[-1] != float('inf') else -1
