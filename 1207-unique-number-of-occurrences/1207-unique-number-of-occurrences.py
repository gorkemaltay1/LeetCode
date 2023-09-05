class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        setArr = set(arr)
        occurenceList = list()
        for i in setArr:
            occurenceList.append(arr.count(i))
        
        if len(list(set(occurenceList))) == len(occurenceList):
            return True
        return False
            