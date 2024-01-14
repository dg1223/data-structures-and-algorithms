class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)

        first_max = heappop(heap) * (-1)
        second_max = heappop(heap) * (-1)

        return (first_max-1)*(second_max-1)