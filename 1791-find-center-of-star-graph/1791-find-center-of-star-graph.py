class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count0 = 0
        count1 = 0
        countCheck = len(edges)
        for i in edges:
            if edges[0][0] in i:
                count0 += 1
            elif edges[0][1] in i:
                count1 += 0
        if count0 == countCheck:
            return edges[0][0]
        return edges[0][1]