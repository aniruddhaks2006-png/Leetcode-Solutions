# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxcount=[0]
        count=1
        def find(root,count):
            if root==None:
                return None
            if count>maxcount[0]:
                maxcount[0]=count
            find(root.left,count+1)
            find(root.right,count+1)
        find(root,count)
        return maxcount[0]
