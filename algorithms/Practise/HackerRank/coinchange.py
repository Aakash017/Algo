"""

n=3
coins=[8,3,2,1]

[-1,-1,-1,-1]
[ 0, 1, 2, 3]
[0, 1, 1+1, 1+1, 2,4,]

# Find total no for each element till n
n=10
coins=[2,5,3,6]
[0,1,2,3,4,5]
l[0]=0
l[1]=0
l[2]=1
l[3]=1
l[4]=2
l[5]=


"""
amount = 4
coins = [1,2,3]
l = [0 for _ in range(amount + 1)]
l[0] = 1

a = [[0 for _ in range(amount)] for i in coins]
for i in range(len(coins)):
    a[i][0] = 1
    for j in range(1, amount):
        if coins[i] > j:
            a[i][j] = a[i - 1][j]
        else:
            a[i][j] = a[i - 1][j] + a[i][j - coins[i]]

print(a)
# https://www.hackerrank.com/challenges/coin-change/editorial
