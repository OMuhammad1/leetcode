class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        oneZero = False
        prod = 1
        for num in nums: 
            if num == 0:
                if oneZero:
                    return [0] * len(nums)
                oneZero = True
            else:
                prod *= num
        
        for i in range(len(nums)):
            if oneZero:
                if nums[i] == 0:
                    nums[i] = int(prod)
                else:
                    nums[i] = 0
            else:
                nums[i] = int(prod / nums[i])
        
        return nums

        