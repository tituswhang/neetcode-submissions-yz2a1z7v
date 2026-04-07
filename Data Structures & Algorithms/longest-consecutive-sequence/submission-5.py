class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = True
        
        longest = 1
        count = 1
        prev = -sys.maxsize
        for key in sorted(freq):
            if key - prev == 1 and prev != -sys.maxsize:
                count += 1
                
                if count > longest:
                    longest = count

            if abs(key - prev) != 1:
                count = 1

            prev = key

        return longest

        # if longest > 0:
        #     return longest + 1
        # else:
        #     return longest