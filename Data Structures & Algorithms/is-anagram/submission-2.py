class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for c in s:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] +=1

        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1

        for c in dict:
            if dict[c] != 0:
                return False

        return True