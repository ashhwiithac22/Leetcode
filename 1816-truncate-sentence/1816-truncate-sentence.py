class Solution(object):
    def truncateSentence(self, s, k):
        word = s.split()
        answer = ""
        for i in range(k):
            if i > 0:
                answer += " "
            answer += word[i]
        return answer