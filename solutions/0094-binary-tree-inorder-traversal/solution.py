# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def move(root):
            if root==None:
                return a
            move(root.left)
            a.append(root.val)
            move(root.right)
        a=[]
        move(root)
        return  a
            
