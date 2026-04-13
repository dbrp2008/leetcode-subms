# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        count = 1
        while curr and curr.next:
            count += 1
            curr = curr.next
        k = k % count
        if count == 1 or k == 0:
            return head
        curr.next = head
        steps = count-k-1
        new_tail = head
        for i in range(steps):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head