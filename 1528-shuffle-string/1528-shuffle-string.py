class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        stringList = list(map(str,s))
        targetList = list()
        dictionary = dict(sorted(zip(indices,stringList)))
        for i in dictionary:
            targetList.insert(i,dictionary[i])
                
        return "".join(targetList)