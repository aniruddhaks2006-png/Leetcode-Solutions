# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        a=[]
        while p!=None:
            a.append(p.val)
            p=p.next
        a.sort()
        q=head
        i=0
        while q!=None:
            q.val=a[i]
            i+=1
            q=q.next
        return head
