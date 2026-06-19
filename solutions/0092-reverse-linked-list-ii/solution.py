# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        m=head
        a=[]
        while m!=None:
           a.append(m.val)
           m=m.next
        a[left-1:right]=a[left-1: right][::-1]
        i=0
        head1=head
        while head1!=None:
         head1.val=a[i]
         i+=1
         head1=head1.next
        return head
