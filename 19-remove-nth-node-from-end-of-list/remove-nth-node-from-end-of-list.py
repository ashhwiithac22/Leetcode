class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        if count == n:
            head = head.next

        curr = head
        while curr:
            if count == n + 1: #stop before the element that need to be removed
                curr.next = curr.next.next
                break
            curr = curr.next
            count -= 1
        return head


