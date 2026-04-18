class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonals = [[] for i in range(m + n - 1)]
        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        result = []
        for k in range(len(diagonals)):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])
            else:
                result.extend(diagonals[k])
        return result
