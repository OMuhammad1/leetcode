class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        curr = dummy 
        carry = 0
        summ = 0

        while l1 or l2:
            first = 0
            second = 0
            if l1:
                first = l1.val 
                l1 = l1.next
            if l2:
                second = l2.val 
                l2 = l2.next

            add = first + second + carry 

            if add > 9: 
                carry = add // 10 
                add = add % 10  
            else: 
                carry = 0 
            
            curr.next = ListNode(add)
            curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(1)
        
        return dummy.next

            


            
            
            