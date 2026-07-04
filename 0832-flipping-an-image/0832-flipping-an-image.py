class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr_rev = []
        flipped = []
        for subarr in image:
            arr_rev.append(subarr[::-1])
        for arrsub in arr_rev:
            new = []
            for i in arrsub:
                if i == 1: 
                    new.append(0)
                else:
                    new.append(1)
            flipped.append(new)
        return flipped     
        