class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        nums=[]
        while head:
            nums.append(head.val)
            head=head.next

        def build(low,high):
            if low>high:
                return None

            mid=(low+high)//2
            root=TreeNode(nums[mid])

            root.left=build(low,mid-1)
            root.right=build(mid+1,high)

            return root

        return build(0,len(nums)-1)
