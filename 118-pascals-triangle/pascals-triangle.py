class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        row = []
        for i in range(numRows):
            row.append(1)
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j] + row[j-1]
            final.append(list(row))
        return final
