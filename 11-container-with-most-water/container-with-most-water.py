class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        area = (r - l) * min(height[l], height[r])

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[r] > height[l]: 
                l += 1
            else:
                r -= 1
            
        return max_area


        

        