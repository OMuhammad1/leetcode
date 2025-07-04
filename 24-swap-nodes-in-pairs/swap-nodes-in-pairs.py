class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next

            first.next = second.next
            second.next = first
            curr.next = second

            curr = first

        return dummy.next
