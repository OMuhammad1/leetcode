class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        maxSum = -1000000

        for i in range(len(nums) - 1, -1, -1):
            sum_ += nums[i] 
            maxSum = max(sum_, maxSum)
            if sum_ < 0:
                sum_ = 0
        
        return maxSum 
        