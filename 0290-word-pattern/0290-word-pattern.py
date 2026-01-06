class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        p_map = {}
        w_map = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in p_map:
                if p_map[p] != w:
                    return False
            else:
                p_map[p] = w

            if w in w_map:
                if w_map[w] != p:
                    return False
            else:
                w_map[w] = p
        return True
        
        

       