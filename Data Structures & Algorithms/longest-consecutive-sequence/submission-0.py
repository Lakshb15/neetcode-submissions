class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique = set(nums)
        for num in unique:
            if num - 1 not in unique:
                current = num
                length = 1
                while current + 1 in unique:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest