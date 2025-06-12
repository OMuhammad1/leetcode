class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        res = []
        heapq.heapify(arr)

        for point in points:
            euc = math.sqrt(point[0] * point[0] + point[1] * point[1])
            heapq.heappush(arr, (euc, point[0], point[1]) )

        for i in range(k):
            euc, x, y = heapq.heappop(arr)
            res.append( [x, y] )
        
        return res
        