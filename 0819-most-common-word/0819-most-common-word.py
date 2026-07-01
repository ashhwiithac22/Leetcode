class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        words = paragraph.lower().split()
        word_count = 0
        ans = ""
        for word in words:
            if word not in banned:
                if words.count(word) > word_count:
                    word_count = words.count(word)
                    ans = word
        return ans