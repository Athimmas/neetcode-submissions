# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        if(head.next == None and n == 1):
            return head.next
        elif (head.next == None and n == 0):
            return head

        i = n 

        ahead = head

        while i > 0:
            ahead = ahead.next
            i -= 1

        if ahead == None:
            return head.next

        cur = head
        prev = head
        first = True

        while ahead:
            prev = cur
            ahead = ahead.next
            cur = cur.next
            

        prev.next = cur.next

        return head
            