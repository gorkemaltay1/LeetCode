class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        list1 = list()
        for i in grid:
            list1 += i
        return len(list(filter(lambda x: (x < 0), list1)))
        