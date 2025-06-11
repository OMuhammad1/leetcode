class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter = {}
        l = 0
        maxL = 0

        for r in range(len(s)):
            if s[r] in letter:
                letter[s[r]] += 1
            else:
                letter[s[r]] = 1
            
            while (r - l + 1) - max(letter.values()) > k:
                letter[s[l]] -= 1
                l += 1
            
            maxL = max(maxL, r-l+1)
        
        return maxL


        
        