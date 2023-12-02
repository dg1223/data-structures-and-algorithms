def search(self, nums: List[int], target: int) -> int:
	length = len(nums)

	# if array is empty or only have 1 element,
	# no need to perform binary search
	if length == 0 or (length == 1 and nums[0] != target):
		return -1
	elif nums[0] == target:
		return 0
	
	
	left = 0
	right = length - 1
	while left <= right:
		mid = (left + right) // 2
		mid_val = nums[mid]
		if mid_val == target:
			return mid
		elif mid_val > target:
			right = mid - 1
		else:
			left = mid + 1
	
	return -1
	