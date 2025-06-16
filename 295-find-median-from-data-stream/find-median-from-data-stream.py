class MedianFinder:

    def __init__(self):
        self.neg = [] #min heap
        self.pos = [] #max heap
        heapq.heapify(self.neg)
        heapq.heapify(self.pos)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.neg, -num)

        if self.neg and self.pos and (-self.neg[0] > self.pos[0]):
            val = -1 * heapq.heappop(self.neg)
            heapq.heappush(self.pos, val)
        
        if len(self.neg) > len(self.pos) + 1:
            val = -1 * heapq.heappop(self.neg) 
            heapq.heappush(self.pos, val)
        
        if len(self.pos) > len(self.neg) + 1:
            val = -1 * heapq.heappop(self.pos)
            heapq.heappush(self.neg, val) 

    def findMedian(self) -> float:
        if len(self.pos) > len(self.neg):
            return self.pos[0]
        elif len(self.neg) > len(self.pos):
            return -self.neg[0]
        else:
            return (self.pos[0] - self.neg[0]) / 2 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()