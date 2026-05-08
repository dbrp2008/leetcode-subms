class Solution:
    def isValid(self, s: str) -> bool:
        stuff_thats_bracketing = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in stuff_thats_bracketing:
                top_element = stack.pop() if stack else '#'
                if stuff_thats_bracketing[char] != top_element:
                    return False
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False