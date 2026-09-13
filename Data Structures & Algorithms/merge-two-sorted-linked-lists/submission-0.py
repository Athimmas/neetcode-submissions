# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ret = ListNode(0)
        acc = ret

        while list1 and list2:
            if list1.val < list2.val:
                ret.next = list1
                list1 = list1.next
            else:
                ret.next = list2
                list2 = list2.next

            ret = ret.next

        while list1:
            ret.next = list1
            list1 = list1.next
            ret = ret.next

        while list2:
            ret.next = list2
            list2 = list2.next
            ret = ret.next

        return acc.next
            

            
