class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for n in nums:
            if n in count:
                count[n] = count[n] + 1
            else:
                count[n] = 1


        for key in count:
            if count[key] > 1:
                return True
        
        return False
         