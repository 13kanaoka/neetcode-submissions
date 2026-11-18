# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        queue = collections.deque()
        queue.append(root)

        while queue:
            qLen = len(queue)
            currLevel = []
            for _ in range(qLen):
                currNode = queue.popleft()
                if currNode:
                    queue.append(currNode.left)
                    queue.append(currNode.right)
                    currLevel.append(currNode.val)
            if currLevel:
                res.append(currLevel)
        return res