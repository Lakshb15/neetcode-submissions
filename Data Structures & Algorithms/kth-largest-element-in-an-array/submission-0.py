import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        output = []
        nums2 = [-x for x in nums]
        heapq.heapify(nums2)

        for i in range(k):
            temp = heapq.heappop(nums2)
            output.append(temp)

        return -(output[-1])