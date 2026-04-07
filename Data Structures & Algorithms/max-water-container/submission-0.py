class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(0, len(heights) - 1):
            for j in range(i + 1, len(heights)):
                l = 0
                if heights[i] < heights[j]:
                    l = heights[i]
                else:
                    l = heights[j]
                
                area = l * (j - i)

                if area > max:
                    max = area

        return max
