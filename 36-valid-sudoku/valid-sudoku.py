class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        boxes = []
        for i in range(9):
            rows.append(set())
            columns.append(set())
            boxes.append(set())
        for i in range(9):
            for j in range(9):
                boxy = board[i][j]
                if boxy == ".":
                    continue
                xbox = (i//3)*3 + (j//3)
                if boxy in rows[i] or boxy in columns[j] or boxy in boxes[xbox]:
                    return False
                rows[i].add(boxy)
                columns[j].add(boxy)
                boxes[xbox].add(boxy)
        return True