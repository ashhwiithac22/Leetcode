class Solution(object):
    def plusOne(self, digits):
        array = []
        str1 = ""
        for d in digits:
            str1 += str(d)
        number =str(int(str1) +1)
        for num in number:
            array.append(int(num))
        return array
