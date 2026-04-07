class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        for c in t:
            if c not in count:
                return False
            else:
                count[c] -= 1

        for key in count:
            if count[key] is not 0:
                return False
        
        return True
        