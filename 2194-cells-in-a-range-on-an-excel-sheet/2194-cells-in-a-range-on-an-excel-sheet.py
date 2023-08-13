class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        zart = s.split(":")
        asciiList = list()
        finalList = list()
        finalestList = list()
        for i in zart:
            asciiList.append(ord(i[0]))
        
        for i in range(asciiList[0],asciiList[1]+1):
            finalList.append(chr(i))
        
        for i in range(len(finalList)):
            for j in range(int(zart[0][1]),int(zart[1][1])+1):
                finalestList.append(finalList[i] + str(j))
        return finalestList