class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set([*sentence])
        alphabet = "abcdefghijklmnoprstuvyzqxw"
        alphabet = set([*alphabet])
        if sentence == alphabet:
            return True
        else:
            return False
            