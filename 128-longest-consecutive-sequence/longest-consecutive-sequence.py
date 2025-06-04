class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxL = 0

        for num in numbers: 
            if num - 1 in numbers:
                continue 
            i = 1
            longest = 1
            while True:
                if num + i not in numbers:
                    break
                i += 1
                longest += 1

            maxL = max(longest, maxL)
        
        return maxL
            


        