# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        Sum = 0
        Carry = 0
        ret = ListNode(0)
        cur = ret

        while l1 and l2:
            Sum = l1.val + l2.val + Carry
            Carry = Sum // 10
            Result = Sum % 10

            ans = ListNode(Result)
            cur.next = ans

            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l1:
            result = l1.val + Carry
            Sum = result % 10
            Carry = result // 10
            l = ListNode(Sum)
            cur.next = l
            cur = cur.next
            l1 = l1.next
        
        while l2:
            result = l2.val + Carry
            Sum = result % 10
            Carry = result // 10
            l = ListNode(Sum)
            cur.next = l
            cur = cur.next
            l2 = l2.next

        
        if Carry:
            one = ListNode(1)
            cur.next = one
            return ret.next

        return ret.next

