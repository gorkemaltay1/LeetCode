class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = list()
        index = 0
        for i in words:
            if x in i:
                indices.append(index)
            index += 1
        return indices