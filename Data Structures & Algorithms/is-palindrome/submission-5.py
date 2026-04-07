class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and s[i].isalnum() == False:
                i += 1

            while i < j and s[j].isalnum() == False:
                j -= 1

            print(str(i) + " " + str(j))

            if i > j or i >= len(s) or j < 0:
                return True

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True