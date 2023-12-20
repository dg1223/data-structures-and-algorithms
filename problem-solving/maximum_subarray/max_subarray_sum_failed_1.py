class Solution:
    def has_overlap(self, arr_1, arr_2):
        set_1 = set(arr_1)
        set_2 = set(arr_2)
        set_3 = set_1.union(set_2)
        
        return len(set_3) < len(set_1) + len(set_2)

    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        max_item_idx = nums.index(max(nums))

        maxsum_1 = nums[0]
        subarray_sum = 0
        indices_1 = []
        for idx in range(max_item_idx, -1, -1):
            subarray_sum += nums[idx]
            if subarray_sum >= maxsum_1:
                maxsum_1 = subarray_sum
                indices_1.append(idx)
        
        print(f"{maxsum_1 = }")
        print(indices_1)

        if max_item_idx == length - 1:
            return maxsum_1
            # start = min(indices_1)
            # end = max_item_idx
            # return sum((nums[idx] for idx in range(start, end+1)))
            
        maxsum_2 = nums[0]
        subarray_sum = 0
        indices_2 = []
        for idx in range(max_item_idx, len(nums)):
            subarray_sum += nums[idx]
            if subarray_sum >= maxsum_2:
                maxsum_2 = subarray_sum
                indices_2.append(idx)
        
        print(f"{maxsum_2 = }")
        print(indices_2)

        if max_item_idx == 0:
            return maxsum_2
            # start = max_item_idx
            # end = max(indices_2)
            # return sum((nums[idx] for idx in range(start, end+1)))

        # return maxsum_1 if maxsum_1 > maxsum_2 else maxsum_2

        start = 0
        end = 0
        
        if self.has_overlap(indices_1, indices_2) or maxsum_1 == maxsum_2:
            print("overlap")
            start = min(indices_1)
            end = max(indices_2)
        elif maxsum_1 > maxsum_2:
            start = min(indices_2)
            end = max_item_idx
        else:
            start = max_item_idx
            end = max(indices_2)

        return sum((nums[idx] for idx in range(start, end+1)))