class Solution(object):
    def isPalindrome(self, head):
        li = []
        while head:
            li.append(head.val)
            head = head.next

        return li == li[::-1]
        


        
