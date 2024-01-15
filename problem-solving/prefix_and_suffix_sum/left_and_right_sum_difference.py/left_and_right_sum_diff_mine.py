class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = []
        rightsum = []

        length = len(nums)

        leftsum.append(0)
        for idx in range(length-1):
            leftsum.append(nums[idx] + leftsum[idx])

        rightsum.append(0)
        rsum_idx = 0
        for idx in range(length - 1, 0, -1):
            rightsum.append(nums[idx] + rightsum[rsum_idx])
            rsum_idx += 1

        rightsum = rightsum[::-1]

        answer = [abs(leftsum[idx] - rightsum[idx]) for idx in range(length)]

        return answer