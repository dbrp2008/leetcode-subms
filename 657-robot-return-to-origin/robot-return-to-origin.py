class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == "R": x = x+1
            if move == "L": x = x-1
            if move == "U": y = y+1
            if move == "D": y = y-1

        return x == y == 0
        """
        :type moves: str
        :rtype: bool
        """
        