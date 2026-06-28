# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isEqual(left,right):
            if left==None and right==None:
                return True
            if left==None or right==None:
                return False
            return left.val==right.val and isEqual(left.left,right.right) and isEqual(left.right,right.left)
        if root is None:
                return True
        return isEqual(root.left,root.right)
        
