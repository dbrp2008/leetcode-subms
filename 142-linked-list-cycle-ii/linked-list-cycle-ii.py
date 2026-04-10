# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next     
            if slow == fast:
                pos = head
                while pos != slow:
                    pos = pos.next
                    slow = slow.next
                return pos
        return None