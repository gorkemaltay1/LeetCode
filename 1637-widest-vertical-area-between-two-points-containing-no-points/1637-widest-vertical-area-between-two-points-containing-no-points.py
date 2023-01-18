class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sortedList = list(sorted([i[0] for i in points]))
        maxOptimal = 0
        for i in range(len(sortedList)-1):
            if sortedList[i+1]-sortedList[i] > maxOptimal:
                maxOptimal = sortedList[i+1] - sortedList[i]
        return maxOptimal