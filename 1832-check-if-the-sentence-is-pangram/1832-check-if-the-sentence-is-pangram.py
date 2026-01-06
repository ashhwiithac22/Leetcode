class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence1 = set(sentence)
        if len(sentence1) == 26:
            return True
        else:
            return False

        