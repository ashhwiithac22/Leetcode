from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        magazine_count = Counter(magazine)
        for letter in ransomNote:
            if magazine_count[letter] > 0:
                magazine_count[letter] -= 1
            else:
                return False
        return True


        