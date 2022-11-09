"Best Time to Buy and Sell Stock"


def maxProfit(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                profit = max(profit, prices[j] - prices[i])
    print(profit)


maxProfit([7, 1, 5, 3, 6, 4])

r = [0, 0, 0, 0, 0, 0]


def maxProfitOptimised(prices):
    max_profit = 0
    buy = prices[0]
    for price in prices:
        buy = min(buy, price)
        max_profit = max(max_profit, price - buy)
    return max_profit


print(maxProfitOptimised([7, 1, 5, 3, 6, 4]))
