# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        arr = [] 
        res = ListNode(0)
        curr = res
        heapq.heapify(arr)

        if not lists:
            return curr.next

        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush( arr,
                ( lists[i].val, i, lists[i] )
                )
        

        while arr: 
            val, index, ll = heapq.heappop(arr)
            curr.next = ll
            curr = curr.next

            if ll.next:
                ll = ll.next
            
                heapq.heappush(arr, 
                    (ll.val, index, ll)
                )

        return res.next

