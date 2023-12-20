# O(N^2)

class Solution:
    # def update_maxsum(self, subsum, maxsum):
    #     maxsum = subsum if subsum > maxsum else maxsum

    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        maxsum = 0
        subarray_sum = 0
        for idx_1, num_1 in enumerate(nums):
            if idx_1 == 0:
                for num_2 in nums:
                    subarray_sum += num_2
                    maxsum = subarray_sum if subarray_sum > maxsum else maxsum
            elif idx_1 == length - 1:Q
                for idx_2 in range(length-1, -1, -1):
                    subarray_sum += num_2
                    maxsum = subarray_sum if subarray_sum > maxsum else maxsum
            else:
                for idx_2, num_2 in enumerate(nums):
                    if idx_2 <= idx_1:
                        for idx_3 in range(length, idx_1-1, -1):
                            subarray_sum = sum((nums(idx) for idx in range(idx_2, idx_3)))
                            maxsum = subarray_sum if subarray_sum > maxsum else maxsum
                    else:
                        subarray_sum = sum((nums(idx) for idx in range(idx_1, idx_2+1)))
                        maxsum = subarray_sum if subarray_sum > maxsum else maxsum

            return maxsum