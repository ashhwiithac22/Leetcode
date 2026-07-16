class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        osum = n * n 
        esum = n * (n + 1)
        rem = -1
        divid = max(osum,esum)
        divi = min(osum,esum)
        while rem!=0:
            rem = divid%divi
            if rem == 0:
                gcd = divi
                break
            divid=divi
            divi=rem
        return divi




        
        