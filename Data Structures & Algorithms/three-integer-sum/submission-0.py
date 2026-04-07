class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []

        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        flag = False

                        for r in res:
                            if nums[i] in r and nums[j] in r and nums[k] in r:
                                flag = True
                                break
                        
                        if flag == False:
                            res.append([nums[i], nums[j], nums[k]])

        return res
        