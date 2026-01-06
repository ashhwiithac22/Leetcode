class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        strs.sort()
        result = ""
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last):
            if first[i] == last[i]:
                result += first[i]
                i += 1
            else:
                break
        return result