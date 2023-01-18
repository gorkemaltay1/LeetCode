class Solution:
    def countPoints(self, rings: str) -> int:
        if len(rings)<6:
            return 0
        else:
            count = 0
            rods = dict()
            for i in range(10):
                rods["B"+str(i)] = 0
                rods["G"+str(i)] = 0
                rods["R"+str(i)] = 0

            for i in range(0,len(rings),2):
                rods[rings[i:i+2]] += 1
            
            for i in range(10):
                if rods["B"+str(i)] != 0 and rods["G"+str(i)] != 0 and rods["R"+str(i)] != 0:
                    count += 1
                else:
                    continue
            return count
        