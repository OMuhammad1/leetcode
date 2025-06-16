class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        temp = [ [] for _ in range(len(nums) + 1) ]

        for num, freq in count.items():
            temp[freq].append(num)
        
        res = []

        for i in range(len(temp)-1 , -1 , -1):
            if temp[i]:
                for num in temp[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        
        return []
        