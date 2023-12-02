def square(number):
	result = number * number
	return result
	
def mySqrt(x: int) -> int:
	root = 0
	left = 0
	right = x
	while left <= right:
		mid = (left + right) // 2
		mid_squared = square(mid)
		if mid_squared == x:
			return mid
		elif mid_squared > x:
			right = mid - 1
		else:
			left = mid + 1
			root = mid
	
	return root

print(mySqrt(0))