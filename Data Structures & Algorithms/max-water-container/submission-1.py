class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            distance = right - left
            height = min(heights[left], heights[right])
            volume = distance * height 
            maxwater = max(maxwater, volume)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
                right -= 1
        return maxwater