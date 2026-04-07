class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        sorted_dict = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))

        return list(sorted_dict.keys())[:k]