class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min = 0
        max = 0
        i = 0

        while i < len(prices):
            if prices[i] < prices[min]:
                min = i

            if prices[i] > prices[min] and i > min:
                max = i
            
            diff = 0

            if max > min:
                diff = prices[max] - prices[min]

            if diff > res:
                res = diff

            i += 1

        return res
        