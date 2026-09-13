# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #print(k)

        def getKth(head,k):

            prev = None


            while k and head:
                prev = head
                head = head.next
                k -= 1

            return head, prev, k == 0

        def reverse(head):

            prev = None
            temp = None

            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp

            return prev

        Kth, prevKth, more = getKth(head,k)

        if not more:
            return head

        prevKth.next = None
        head = reverse(head)

        end = head

        while end.next:
            end = end.next

        end.next = self.reverseKGroup(Kth,k)
        return head

        
