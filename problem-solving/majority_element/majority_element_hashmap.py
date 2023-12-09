# Works even if there is no majority element

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        threshold = length / 2

        freq_map = {}
        freq_map.update(Counter(nums))

        for num, freq in freq_map.items():
            if freq > threshold:
                return num