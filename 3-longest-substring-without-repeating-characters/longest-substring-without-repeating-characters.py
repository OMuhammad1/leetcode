class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        maxLength = 0
        curr = set()

        if not s:
            return length
        
        left, right = 0,0 

        while right < len(s):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            right += 1
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength - 1

        