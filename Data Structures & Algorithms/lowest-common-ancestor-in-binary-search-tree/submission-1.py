# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val: # in the left subtree
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val: # in the right subtree
                curr = curr.right
            elif curr.val == p.val:
                return p
            elif curr.val == q.val:
                return q
            else:
                return curr

