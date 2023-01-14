class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelCount = 0
        jewelType = list(map(str,jewels))
        for i in stones:
            if i in jewelType:
                jewelCount += 1
        return jewelCount