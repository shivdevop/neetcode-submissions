# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=n
        a=head
        while temp>0:
            a=a.next 
            temp-=1

        if not a:
            return head.next     
        
        b=head
        while a.next:
            a=a.next
            b=b.next

        b.next=b.next.next 

        return head    



        