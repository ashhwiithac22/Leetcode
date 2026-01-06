class Solution(object):
    def isIsomorphic(self, s, t):
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in s_map:
                if s_map[a] != b:
                    return False
            else:
                s_map[a] = b

            if b in t_map:
                if t_map[b] != a:
                    return False
            else:
                t_map[b] = a
        return True
        
        