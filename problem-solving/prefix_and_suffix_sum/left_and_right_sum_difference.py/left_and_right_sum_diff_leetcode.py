class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = 0
        suffix = sum(nums)
        result = []
        
        for num in nums:
            prefix += num
            result.append(abs(prefix - suffix))
            suffix -= num

        return result

'''
nums = [10,4,8,3]
Output: [15,1,11,22]

prefix = 0
suffix = sum(nums) = 25

iter 1:
	prefix = 0 + nums[1] = 0 + 10 = 10
	output 1: |prefix - suffix| = |10 - 25| = 15
  suffix = 25 - nums[1] = 25 - 10 = 15

iter 2:
	prefix = 10 + nums[2] = 10 + 4 = 14
	output 2: |prefix - suffix| = |14 - 15| = 1
  suffix = 15 - nums[2] = 15 - 4 = 11
'''