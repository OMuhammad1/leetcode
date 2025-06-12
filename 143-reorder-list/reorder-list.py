# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        #Now slow will be at the middle 

        #Detatch and flip second half
        start = slow.next
        slow.next = None
        prev = None
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp

        
        #Now merge head and prev 
        curr = head 
        #prev 
        while prev:
            temp = curr.next
            temp2 = prev.next

            curr.next = prev
            prev.next = temp

            curr = temp
            prev = temp2 


        return head