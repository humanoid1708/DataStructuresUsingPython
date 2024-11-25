def BuyAndSell(prices):
    profit = 0
    for i in range(0, len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
    return profit

arr = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(BuyAndSell(arr))
