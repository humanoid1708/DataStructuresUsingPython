def BuyAndSell(prices):
    profit = 0
    for i in range(0, len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
    return profit

def buy_and_sell_stock_once(prices):
  cp = 0
  profit = 0
  while cp < len(prices):
      sp = cp
      while sp < len(prices):
          if prices[sp] - prices[cp] > profit:
              profit = prices[sp] - prices[cp]
          sp += 1
      cp +=1
  return profit

# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price)
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
  return max_profit

arr = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(BuyAndSell(arr))
