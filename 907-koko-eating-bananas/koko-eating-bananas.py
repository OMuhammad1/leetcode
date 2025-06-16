class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high: 
            mid = (low + high) // 2

            temp = 0
            for pile in piles: 
                temp += math.ceil(pile/mid)
            
            if temp > h:
                low = mid + 1
            elif temp <= h:
                high = mid - 1
        
        return low 
            



        