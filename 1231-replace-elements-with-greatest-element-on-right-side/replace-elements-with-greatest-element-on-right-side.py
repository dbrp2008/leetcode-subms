class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        if len(arr) == 1:
            arr[0] = -1
        for i in range(len(arr) -1, -1, -1):
            current = arr[i]
            arr[i] = max
            if current > max:
                max = current
        return arr