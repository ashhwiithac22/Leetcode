class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            count = {}
            length = 0
            for j in range(i, len(s)):
                if s[j] not in count:
                    count[s[j]] = 1
                else:
                    count[s[j]] += 1
                if count[s[j]] > 2:
                    break
                length += 1
                if length > ans:
                    ans = length
        return ans



        