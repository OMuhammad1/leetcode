class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            j = i + 1 
            k = len(nums) - 1

            while j < k: 
                score = nums[i] + nums[j] + nums[k] 

                if score > 0:
                    k -= 1
                elif score < 0: 
                    j += 1
                else: 
                    res.append([ nums[i], nums[j], nums[k] ] )

                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    
                    j += 1
                    k -= 1

        return res 
                    


            
        
        