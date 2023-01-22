class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        examScores = dict()
        finalList = list()
        for i in range(len(score)):
            examScores[i] = score[i][k]
        for w in sorted(examScores,key=examScores.get,reverse=True):
            finalList.append(score[w])
        return finalList