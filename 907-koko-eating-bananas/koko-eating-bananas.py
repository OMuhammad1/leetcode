import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles) #O(n) 
        min_speed = high


        while low <= high: 
            mid = (low + high) // 2

            tHours = 0 

            for time in piles:
                tHours += math.ceil( time / mid )

            if tHours > h:
                low = mid + 1 
            elif tHours <= h:
                high = mid - 1
            
        
        return low

