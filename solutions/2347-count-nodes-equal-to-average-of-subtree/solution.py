# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        a=[]
        def search(node):
            if node==None:
                return 0,0
            ls,lc=search(node.left)
            rs,rc=search(node.right)
            total=ls+rs+node.val
            count=lc+rc+1
            if(total//count==node.val):
                a.append(node.val)
            return total,count
        search(root)
        return len(a)
        
