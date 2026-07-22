class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start = startTime.split(':')
        end = endTime.split(':')
        sh = int(start[0])
        sm = int(start[1])
        ss = int(start[2])
        eh = int(end[0])
        em = int(end[1])
        es = int(end[2])
        start_sec = sh * 3600 + sm * 60 + ss
        end_sec = eh * 3600 + em * 60 + es
        return end_sec - start_sec