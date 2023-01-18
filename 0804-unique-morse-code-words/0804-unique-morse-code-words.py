class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseAlphabet=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        morseList = []
        for i in words:
            wordMorse = ""
            for j in i:
                wordMorse += morseAlphabet[alphabet.index(j)]
            morseList.append(wordMorse)
        return len(set(morseList))
            