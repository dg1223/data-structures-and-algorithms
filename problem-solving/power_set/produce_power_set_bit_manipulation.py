def powerset(items):
	result = []
	length = len(items)
	power_set_items = 2**length

	for bit in range(power_set_items):
		subset = []
		for digit in range(length):
			if (bit & (1 << digit) > 0):
				subset.append(items[digit])
		result.append(subset)

	return result

items = ['a', 'b', 'c']
print(powerset(items))