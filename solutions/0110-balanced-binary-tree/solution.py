class Solution:
    def isBalanced(self,root:Optional[TreeNode])->bool:
        def search(node):
            if node==None:
                return 0
            left=search(node.left)
            right=search(node.right)
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return max(left,right)+1
        return search(root)!=-1
