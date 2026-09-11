class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] not in seen:
                seen[nums[i]] = i
            else:
                return [seen[target - nums[i]],i]