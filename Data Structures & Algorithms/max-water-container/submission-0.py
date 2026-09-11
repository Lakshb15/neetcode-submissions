class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = []
        for i, num in enumerate(heights):
            for j in range(i+1, len(heights)):
                distance = j - i
                height = min(num, heights[j])
                volume = distance * height
                maxwater.append(volume)

        return max(maxwater)