"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = Node(0)
        dummy.next = head
        begin = [head]
        prev = dummy
        while begin:
            curr = begin.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next:
                begin.append(curr.next)
            if curr.child:
                begin.append(curr.child)
                curr.child = None
            prev = curr
        head.prev = None
        return head