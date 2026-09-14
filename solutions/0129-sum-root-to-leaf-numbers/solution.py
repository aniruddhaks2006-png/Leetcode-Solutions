# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        a=[]
        def search(node,s):
            if node is  None:
                return
            s+=str(node.val)
            if node.left is None and node.right is None:
                a.append(s)
                return
            search(node.left,s)
            search(node.right,s)
        search(root,"")
        for i in range(len(a)):
            a[i]=int(a[i])
        return sum(a)
        
