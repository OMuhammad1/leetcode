class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        curr = set()
        longest = 1
        left, right = 0, 0

        while right < len(s):
            if s[right] not in curr:
                curr.add(s[right])
            else:
                while s[right] in curr:
                    curr.remove(s[left])
                    left += 1
                curr.add(s[right])
                
            longest = max(longest, len(curr))
            right += 1
        
        return longest
            
        