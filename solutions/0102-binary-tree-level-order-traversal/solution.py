from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root])
        ans=[]
        while q:
            l=[]
            for i in range(len(q)):
             node=q.popleft()
             l.append(node.val)
             if node.left!=None:
                q.append(node.left)
             if node.right!=None:
                q.append(node.right)
            ans.append(l)
        return ans
