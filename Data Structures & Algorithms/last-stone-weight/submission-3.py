import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        rocks = [-x for x in stones]
        heapq.heapify(rocks)
        while len(rocks) > 1:
            largest = -heapq.heappop(rocks)
            second = -heapq.heappop(rocks)
            if largest == second:
                pass
            else:
                new = largest - second
                heapq.heappush(rocks,-new)
            
        if not rocks:
            return 0
        return -(rocks[0])