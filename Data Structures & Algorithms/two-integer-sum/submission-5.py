class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(0, len(nums)):
            dict[target - nums[i]] = i

        for i in range(0, len(nums)):
            if nums[i] in dict and i != dict[nums[i]]:
                l = []
                if i < dict[nums[i]]:
                    l.append(i)
                    l.append(dict[nums[i]])
                else:
                    l.append(dict[nums[i]])
                    l.append(i)
                return l