# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        a=[]
        sumi=0
        def search(node):
            if node==None:
                return 
            a.append(node.val)
            search(node.left)
            search(node.right)
        search(root)
        for num in a:
            if num>=low and num<=high:
                sumi+=num
        return sumi
