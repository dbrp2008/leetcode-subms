class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        n = len(s)
        bucket = [[] for i in range(n+1)]
        for c, i in count.items():
            bucket[i].append(c)
        ans = []
        for i in range(n, -1, -1):
            for c in bucket[i]:
                ans.append(c * i)
        return "".join(ans)