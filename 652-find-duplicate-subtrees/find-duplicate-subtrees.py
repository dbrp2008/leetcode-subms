# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        counts = {}
        def traverse(node):
            if not node:
                return "#"
            left = traverse(node.left)
            right = traverse(node.right)
            signature = f"{left},{right},{node.val}"
            counts[signature] = counts.get(signature, 0) + 1
            if counts[signature] == 2:
                res.append(node)
            return signature
        traverse(root)
        return res