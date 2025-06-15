class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - ord('a')] += 1
            temp2 = tuple(temp)
            if temp2 in groups:
                groups[temp2].append(word)
            else:
                groups[temp2] = [word]
        
        return list(groups.values())
        