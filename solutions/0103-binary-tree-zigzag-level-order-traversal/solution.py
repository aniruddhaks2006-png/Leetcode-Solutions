# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        a=[]
        q=deque([root])
        while q:
            size=len(q)
            c=[]
            for i in range(size):
             x=q.popleft()
             c.append(x.val)
             if x.left:
                q.append(x.left)
             if x.right:
                q.append(x.right)
            a.append(c)
        for i in range(len(a)):
            if i%2==0:
                continue
            a[i]=a[i][::-1]
        return a        
