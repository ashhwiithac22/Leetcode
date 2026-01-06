class Solution(object):
    def frequencySort(self, s):
        hashmap = {}

        for ch in s:
            hashmap[ch] = hashmap.get(ch,0) + 1

        result = ""
        for ch in sorted(hashmap, key = hashmap.get, reverse = True):
            result += ch*hashmap[ch]
        return result
