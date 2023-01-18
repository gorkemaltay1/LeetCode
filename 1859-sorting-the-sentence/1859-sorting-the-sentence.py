class Solution:
    def sortSentence(self, s: str) -> str:
        sList = s.split(" ")
        reversedSList = []
        answer = ""
        for i in sList:
             reversedSList.append(i[::-1])
        sortedsList = sorted(reversedSList)
        for i in sortedsList:
            answer += i[:0:-1] + " "
        return answer[:len(answer)-1]