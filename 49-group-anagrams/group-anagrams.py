class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = {}
        for w in strs:
            key = "".join(sorted(w))
            if key not in ag:
                ag[key] = []
            ag[key].append(w)
        return list(ag.values())