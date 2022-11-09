"""Min Cost Climbing Stairs"""


def minCostClimbingStairs(cost):
    # t =[1,100,1,1,1,100,1,1,100,1]
    # t =[1,100,2,3,3,103,4,5,104,6]
    for step in range(2, len(cost)):
        cost[step] += min(cost[step - 1], cost[step - 2])
    print(min(cost[-1], cost[-2]))


minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
# minCostClimbingStairs([10, 15, 20])
