# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next==None:
            return head
        p1=head
        p2=p1.next
        p1.next=p2.next
        p2.next=p1
        head=p2
        while p1.next!=None and p1.next.next!=None:
            newnode=p1
            p1=p1.next
            p2=p1.next
            p1.next=p2.next
            p2.next=p1
            newnode.next=p2
        return head
