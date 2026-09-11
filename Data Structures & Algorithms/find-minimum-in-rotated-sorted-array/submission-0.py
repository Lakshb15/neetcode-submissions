class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = float("inf")

        while left <= right:

            if nums[left] <= nums[right]:
                minimum = min(minimum, nums[left])
                break

            mid = (left + right) // 2

            if nums[mid] >= nums[left]:
                minimum = min(minimum,nums[left])
                left = mid + 1
            elif nums[mid] <= nums[right]:
                minimum = min(minimum, nums[mid])
                right = mid - 1

        return minimum
                   