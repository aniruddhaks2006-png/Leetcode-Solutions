# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        a=[]
        def search(node,b,sumi):
            if node==None:
                return 0
            if node.left==None and node.right==None and sumi+node.val==targetSum:
                b.append(node.val)
                a.append(b)
                return 0
            b.append(node.val)
            search(node.left,b.copy(),sumi+node.val)
            search(node.right,b.copy(),sumi+node.val)
        search(root,[],0)
        return a
        
