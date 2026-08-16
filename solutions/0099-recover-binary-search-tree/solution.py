class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        first = None
        second = None
        prev = None

        def search(node):
            nonlocal first, second, prev

            if node is None:
                return

            search(node.left)

            if prev is not None and prev.val > node.val:
                if first is None:
                    first = prev

                second = node

            prev = node

            search(node.right)

        search(root)

        first.val, second.val = second.val, first.val
