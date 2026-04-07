class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        for i in range(0, len(strs)):
            skip = False
            
            for l in res:
                if strs[i] in l:
                    skip = True
                    break

            if skip:
                continue
            
            count = {}

            for c in strs[i]:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1

            anagrams = [strs[i]]

            for j in range(i + 1, len(strs)):
                countCopy = count.copy()
                print(countCopy)
                flag = False

                for c in strs[j]:
                    if c in countCopy:
                        countCopy[c] -= 1
                    else:
                        flag = True
                        break
                
                if flag:
                    continue
                
                for n in countCopy:
                    if countCopy[n] != 0:
                        flag = True
                        break;

                if flag == False:
                    anagrams.append(strs[j])
            
            res.append(anagrams)

        return res

        