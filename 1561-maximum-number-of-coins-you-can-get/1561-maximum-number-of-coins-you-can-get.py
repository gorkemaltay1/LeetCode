class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sortedPiles = sorted(piles)
        me = 0
        bob,myPick = 0,len(sortedPiles)-1
        while bob<myPick:
            me += sortedPiles[myPick-1]
            bob += 1
            myPick -= 2
        return me