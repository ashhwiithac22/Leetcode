# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head and not head.next:
            return True
        slow = head
        fast = head

        #finding middle element in linkedlist
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversing second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first_half = head
        second_half_reversed = prev
        while second_half_reversed:
            if first_half.val != second_half_reversed.val:
                return False
            first_half = first_half.next
            second_half_reversed = second_half_reversed.next
        return True

            


        
