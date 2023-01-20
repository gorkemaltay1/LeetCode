class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a = "abcdefgh"
        b = "12345678"
        if (a.index(coordinates[0]) + b.index(coordinates[1])) % 2 == 0:
            return False
        return True
        