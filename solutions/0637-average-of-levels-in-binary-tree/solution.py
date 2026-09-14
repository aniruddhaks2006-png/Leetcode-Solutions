# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        a=[]
        q=deque([root])
        while q:
           sumi=0
           s=len(q)
           for x in range(s):
            p=q.popleft()
            sumi+=p.val
            if p.left:q.append(p.left)
            if p.right:q.append(p.right)
           a.append(sumi/s)
        return a

