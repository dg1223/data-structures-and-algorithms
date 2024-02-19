class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []				
        for idx, num in enumerate(nums):
            if idx == 0:
                prefix.append(1)
            else:
                previous = idx - 1
                prefix.append(nums[previous] * prefix[previous])

        suffix = []
        suffix_counter = 0
        for idx, num in reversed(list(enumerate(nums))):
                if idx == len(nums)-1:
                    suffix.append(1)
                else:
                    next = idx + 1
                    suffix.append(nums[next] * suffix[suffix_counter])
                    suffix_counter += 1

        suffix = suffix[::-1]

        return [ prefix[idx]*suffix[idx] for idx in range(len(prefix))]