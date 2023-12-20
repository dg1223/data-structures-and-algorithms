class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -inf
        subarray_sum = -inf
        for idx, num in enumerate(nums):
            subarray_sum = max(num, subarray_sum + num)
            maxsum = max(maxsum, subarray_sum)

        return maxsum