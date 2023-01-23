class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("U") - moves.count("D") == 0 and moves.count("L") - moves.count("R") == 0:
            return True
        return False