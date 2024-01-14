class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heappush(heap, num)
        
        sorted_array = []

        while heap:
            popped = heappop(heap)
            sorted_array.append(popped)

        return sorted_array