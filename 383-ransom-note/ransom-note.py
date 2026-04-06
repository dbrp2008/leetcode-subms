class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        yes = {}
        for char in magazine:
            if char in yes:
                yes[char] += 1
            else:
                yes[char] = 1
        for char in ransomNote:
            if char in yes and yes[char]>0:
                yes[char] -=1
            else:
                return False
        return True