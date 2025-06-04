class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char)-ord('a')] += 1
            key = tuple(temp)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        return list(groups.values())

        