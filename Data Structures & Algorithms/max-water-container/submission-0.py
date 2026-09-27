class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_height = 0
        while l < r:
            total = (r-l) * min(heights[r], heights[l])
            max_height = max(max_height, total)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_height