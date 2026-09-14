class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev=None

        def search(root):
            nonlocal prev
            if not root:
                return
            left=root.left
            right=root.right
            if prev:
                prev.left=None
                prev.right=root
            prev=root
            search(left)
            search(right)

        search(root)
