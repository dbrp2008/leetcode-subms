class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num == 0:
                count = count
            else:
                if num % 2 == 0:
                    num = num // 2
                    count += 1
                if num % 2 != 0:
                    num = num - 1
                    count += 1
        return count
                