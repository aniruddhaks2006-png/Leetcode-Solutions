# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def leftsum(root):
            if root==None:
                return 0
            if root.left and root.left.left==None and root.left.right==None:
                return root.left.val+leftsum(root.right)
            return leftsum(root.left)+leftsum(root.right)
        x=leftsum(root)
        return x
            
                
        
