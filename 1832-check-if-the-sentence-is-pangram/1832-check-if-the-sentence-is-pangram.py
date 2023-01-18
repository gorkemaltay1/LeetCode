class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set([*sentence])
        alphabet = set([*"abcdefghijklmnoprstuvyzqxw"])
        if sentence == alphabet:
            return True
        else:
            return False
            