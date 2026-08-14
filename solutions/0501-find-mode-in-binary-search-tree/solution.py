# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def search(node):
            if node==None:
                return 
            if node.val not in d:
                d[node.val]=1
            else:
                d[node.val]+=1
            search(node.left)
            search(node.right)
        search(root)
        max_count=max(d.values())
        return [key for key, value in d.items() if value == max_count]
        
