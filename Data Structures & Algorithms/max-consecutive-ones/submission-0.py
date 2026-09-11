class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        count = 0

        for num in nums:
            
            if num == 1:
                count += 1
            else:
                res.append(count)
                count = 0    

        res.append(count)

        return max(res)