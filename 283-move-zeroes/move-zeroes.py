class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0 
        zero = 0

        for i in range( len(nums) ):
            if nums[i] != 0:
                nums[index] = nums[i] 
                index += 1
            else: 
                zero += 1
        
        for i in range(1, zero + 1):
            nums[len(nums) - i] = 0
        


        