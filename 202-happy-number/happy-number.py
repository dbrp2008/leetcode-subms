class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if (n != 1 or n != 7) and n<10:
            return False
        done = set()
        while n != 1:
            if n in done:
                return False
            done.add(n)
            sums = 0
            while n > 0:
                digit = n % 10    
                sums = sums + (digit**2)
                n = n // 10
            n = sums
        return True