class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = []
        heapq.heapify(arr)

        for num, occ in count.items():
            heapq.heappush(arr, (occ, num))
            if len(arr) > k:
                heapq.heappop(arr)

        temp = []

        while arr:
            occ, num = heapq.heappop(arr)
            temp.append(num)
        
        return temp




        