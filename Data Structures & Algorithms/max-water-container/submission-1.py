class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            l = 0

            if heights[i] < heights[j]:
                l = heights[i]
            else:
                l = heights[j]

            area = l * (j - i)

            if area > max:
                max = area

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max
