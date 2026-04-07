class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        freq = []

        for i in range(len(nums) + 1):
            freq.append([])

        for key, val in count.items():
            freq[val].append(key)

        res = []

        for l in freq[::-1]:
            for n in l:
                res.append(n)
                
                if len(res) == k:
                    return res