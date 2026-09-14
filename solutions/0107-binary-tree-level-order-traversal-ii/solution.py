class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q=[root]
        ans=[]

        while q:
            a=[]
            for _ in range(len(q)):
                x=q.pop(0)
                a.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            ans.append(a)

        return ans[::-1]
