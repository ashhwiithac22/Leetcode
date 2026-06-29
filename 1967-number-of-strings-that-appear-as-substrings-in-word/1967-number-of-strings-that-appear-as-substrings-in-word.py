class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for string in patterns:
            if string in word:
                count += 1
        return count

        