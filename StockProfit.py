class BuySellStock:
  # @param prices, a list of stock prices
  # @return index of buy and sell price
  def choiceStocks(self, prices):
    n = len(prices)
    if n == 0:
      return None, None
    if n == 1:
      return 0, 0
    maxPrice = prices[n - 1]
    mpIndex = n - 1
    maxProfit = 0
    for price in range(n):
      currPrice = prices[n - price - 1]
      if currPrice > maxPrice:
        maxPrice = currPrice
        mpIndex = n - price - 1
      currProfit = maxPrice - currPrice
      if currProfit > maxProfit:
        maxProfit = currProfit
        bpIndex = n - price - 1
    return bpIndex, mpIndex

# Driver code to test the program
run = BuySellStock()
print(run.choiceStocks([5,6,7,8,10,3,8,7,11,1,2,11]))
