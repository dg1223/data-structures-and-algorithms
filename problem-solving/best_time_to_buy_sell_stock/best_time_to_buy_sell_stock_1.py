def maxProfit(self, prices: List[int]) -> int:
	length = len(prices)
	if not length or length == 1 or sum(prices) == 0:
		return 0
	
	profit = 0
	for idx in range(length-1):
		if idx == 0:
			buy_idx = idx
			sell_idx = idx + 1

		result = prices[sell_idx] - prices[buy_idx]

		'''
		Algorithm:
		When you have your first potential gain (profit),
		hold that buy price and check if there is any 
		other price that further increases your gains.
		When your result (sell - buy) is -ve, it means
		there's a price that's even lower than your 
		current buy price. So, you replace your current
		buy price with that new price just to check if 
		you can get a better buy price.
		'''
		if result > profit:
			profit = result

		if result < 0:
			buy_idx = sell_idx

		# DRY principle
		sell_idx += 1

	return profit