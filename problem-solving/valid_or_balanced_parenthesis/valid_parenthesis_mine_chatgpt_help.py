class Solution:
    def isValid(self, string: str) -> bool:
        hashmap = { '(': ')', '{': '}', '[': ']' }
        stack = []
        for char in string:
            if char not in hashmap and not stack:
                return False			
           				
            if char in hashmap:
                stack.append(char)

            # The following elif pops the stack regardless of it returning
            # true or not. Therefore, if char is in hashmap, we don't need
            # to explicitly pop the stack.
            elif stack and char != hashmap[stack.pop()]:
                return False                    

        # equivalent to return len(stack) == 0
        return not stack
