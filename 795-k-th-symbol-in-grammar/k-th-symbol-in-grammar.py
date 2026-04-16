class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        parent_k = (k + 1) // 2
        parent_val = self.kthGrammar(n - 1, parent_k)
        
        if k % 2 == 1:
            return parent_val
        else:
            return 1 - parent_val 