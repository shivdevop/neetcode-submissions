"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}  # Use a normal dict
        temp=head 
        
        while temp:
            new_node=Node(temp.val)
            node_map[temp]=new_node
            temp=temp.next

        temp2=head
        dummy=Node(0)
        curr=dummy

        while temp2:
            
            curr.next=node_map[temp2]
            curr=curr.next

            # curr.next=temp2.next
            # curr.random=temp2.random
            #above two lines are mistakes
            # we cant assign curr.next and curr.random to original linked list, it should link be to copied ones
            
            curr.next=node_map[temp2.next] if temp2.next else None
            curr.random=node_map[temp2.random] if temp2.random else None

            temp2=temp2.next

        return dummy.next    

        