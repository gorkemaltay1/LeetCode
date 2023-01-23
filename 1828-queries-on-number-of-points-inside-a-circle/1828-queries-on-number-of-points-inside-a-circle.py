class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        finalList = []
        for j in queries:
            count = 0
            for i in points:
                if (i[0] - j[0])**2 + (i[1]-j[1])**2 <= j[2]**2:
                    count += 1
            finalList.append(count)
        return finalList