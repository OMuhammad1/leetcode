"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otc = {None : None} 

        curr = head

        while curr: 
            copy = ListNode(curr.val) 
            otc[curr] = copy
            curr = curr.next
        
        curr = head 

        while curr:
            node = otc[curr]
            node.next = otc[curr.next]
            node.random = otc[curr.random]
            curr = curr.next
        
        return otc[head]

        