class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        arr = []

        for stone in stones:
            arr.append(-1*stone)
        
        heapq.heapify(arr)


        while arr: 
            one = heapq.heappop(arr)
            if not arr:
                return -1*one
            two = heapq.heappop(arr)

            if one < two:
                heapq.heappush(arr, one - two)
        
        return 0


        