class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def remove_leaf(root):
            if root is None:
                return None
            root.left = remove_leaf(root.left)
            root.right = remove_leaf(root.right)
            if root.val == 0 and root.left is None and root.right is None:
                return None
            return root
        return remove_leaf(root)
