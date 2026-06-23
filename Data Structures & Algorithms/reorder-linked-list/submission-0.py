# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 

        #now slow will be at the middle node 

        tail=slow.next
        slow.next=None 

        #reverse the second linked list now 
        prev=None

        while tail:
            temp=tail.next 
            tail.next=prev
            prev=tail 
            tail=temp

        tail=prev #so tail is now at the last node 
        
        first=head
        while tail:
            a,b=first.next,tail.next

            first.next=tail
            tail.next=a
            first=a
            tail=b       
        