class Solution(object):
    def maxDepth(self, s):
        result = 0
        current = 0
        for c in s:
            if c == '(':
                current += 1
            elif c == ')':
                current -= 1
            
            result = max(result,current)
        return result
        
                
        