class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = {}
        left = 0
        max_length = 0
        for right, char in enumerate(s):
            if char in string and string[char] >= left:
                left = string[char] + 1
            string[char] = right
            max_length = max(max_length, right-left+1)
        return max_length