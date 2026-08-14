# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        a=[]
        def search(node):
            if node==None:
                return 
            a.append(node.val)
            search(node.left)
            search(node.right)
        search(root)
        num=a[0]
        for x in a:
            if x!=num:
                return False
        return True
