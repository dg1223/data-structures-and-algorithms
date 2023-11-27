class Solution:
    def isValid(self, string: str) -> bool:
        hashmap = { '(': ')', '{': '}', '[': ']' }
        stack = []
        length = len(string)
        for idx in range(length):
            current_char = string[idx]
            if idx == 0 and current_char not in hashmap:
                return False						
            if current_char in hashmap:
                stack.append(current_char)
            elif stack:
                top_char_in_stack = stack[-1]
                if current_char == hashmap[top_char_in_stack]:
                    stack.pop()
                else:
                    return False
            else:
                    return False
                    

        return len(stack) == 0
