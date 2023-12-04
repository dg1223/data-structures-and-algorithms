# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        left = 1
        right = n	
        first_bad_version = 1
        
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                first_bad_version = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return first_bad_version