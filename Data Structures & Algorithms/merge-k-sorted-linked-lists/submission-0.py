# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        def merge(list1,list2):

            res = ListNode(0)
            h = res

            while list1 and list2:
                if list1.val <= list2.val:
                    res.next = list1
                    list1 = list1.next
                else:
                    res.next = list2
                    list2 = list2.next

                res = res.next

            if list1:
                while list1:
                    res.next = list1
                    list1 = list1.next
                    res = res.next

            if list2:
                while list2:
                    res.next = list2
                    list2 = list2.next
                    res = res.next

            res.next = None
            return h.next

        ret = lists[0]
        for i in range(len(lists) - 1):
            ret = merge(ret,lists[i+1])

        return ret