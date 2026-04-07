class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 0

        res = []

        for i in range(0, k):
            maximum = 0
            index = 0

            for key in freq:
                if freq[key] >= maximum:
                    index = key
                    maximum = freq[key]
            
            res.append(index)
            freq.pop(index)

        return res