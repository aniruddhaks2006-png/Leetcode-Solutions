# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        c=0
        def ifsum(node,c):
            if node==None:
                return False
            if c+node.val==targetSum and node.left==None and node.right==None:
                return True
            return ifsum(node.left,c+node.val) or ifsum(node.right,c+node.val)
        return ifsum(root,c)
        
