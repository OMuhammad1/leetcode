class Solution:
    def trap(self, height: List[int]) -> int:
        collected = 0
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]

        while left < right: 

            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])

                if ( - height[left] + min(maxL, maxR) > 0):
                    collected += - height[left] + min(maxL, maxR)
            else: 
                right -= 1
                maxR = max(maxR, height[right])
                if (- height[right] + min(maxL, maxR) > 0):
                    collected += - height[right] + min(maxL, maxR)
                    

        return collected 


        



        