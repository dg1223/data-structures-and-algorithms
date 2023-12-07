'''
O(N) time and space
'''

from collections import Counter

class Solution:
    def longestPalindrome(self, string: str) -> int:
        length = len(string)
        if length == 1:
            return 1

        hashmap = {}
        hashmap.update(Counter(string))

        odd = sum(( 1 for char in hashmap if hashmap[char] % 2 == 1  ))

        return (length - odd + 1) if odd else length

# bbb, ababacd
print(longest_palindrome_length("abc"))