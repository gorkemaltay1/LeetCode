class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startBin = bin(start).replace("0b","")
        goalBin = bin(goal).replace("0b","")
        equalledBin = abs(len(startBin)-len(goalBin))*"0" + (goalBin if len(goalBin)<len(startBin) else startBin)
        count = 0
        for i in range(1,len(equalledBin)+1):
            if len(startBin)<=len(goalBin):
                if equalledBin[-i] != goalBin[-i]:
                    count += 1
                else:
                    continue
            if len(goalBin)<len(startBin):
                if equalledBin[-i] != startBin[-i]:
                    count += 1
                else:
                    continue
        return count
                
        