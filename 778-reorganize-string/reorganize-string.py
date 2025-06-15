class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = {}
        res = ""
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
            
        arr = []
        heapq.heapify(arr)

        for let, occ in letters.items():
            heapq.heappush(arr, (-occ, let))

        temp = ''
        tempOcc = 0
        while arr:
            occ, letter = heapq.heappop(arr)
            res += letter

            if tempOcc + 1 < 0: 
                heapq.heappush(arr, (tempOcc + 1, temp))

            temp = letter 
            tempOcc = occ
        
        if len(res) == len(s):
            return res
        return ""
        