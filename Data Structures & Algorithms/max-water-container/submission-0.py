class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left = 0
        right = n - 1
        res = []

        while left < right:
            
            area = (right - left) * min(heights[left], heights[right])

            res.append(area)

            if heights[left] <= heights[right]:
                left += 1

            elif heights[right] < heights[left]:
                right -= 1

        return max(res)




        