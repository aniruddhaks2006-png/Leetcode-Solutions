# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a=[]
        b=[]
        def search(node):
            if node is None:
                return None
            if node.left==None and node.right==None:
             a.append(node.val)
             return
            search(node.left)
            search(node.right)
        def search1(node):
            if node is None:
                return
            if node.left==None and node.right==None:
             b.append(node.val)
             return
            search1(node.left)
            search1(node.right)
        search(root1)
        search1(root2)
        return a==b
        
