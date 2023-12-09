from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        frequency = {}
        frequency.update(Counter(nums))

        return any(value > 1 for value in frequency.values())
        