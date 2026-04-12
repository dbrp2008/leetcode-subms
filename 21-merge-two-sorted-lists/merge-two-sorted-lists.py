# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        for i in [list1, list2]:
            curr = i
            while curr:
                vals.append(curr.val)
                curr = curr.next
        vals.sort()
        dummy = ListNode(0)
        curr = dummy
        for i in vals:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next