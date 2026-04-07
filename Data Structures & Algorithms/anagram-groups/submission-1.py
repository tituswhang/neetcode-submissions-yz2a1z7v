class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in range(0, len(strs)):
            key = "".join(sorted(strs[i]))

            if key not in d:
                d[key] = []

            d[key].append(i)

        res = []

        for key in d:
            l = []

            for value in d[key]:
                l.append(strs[value])

            res.append(l)

        return res