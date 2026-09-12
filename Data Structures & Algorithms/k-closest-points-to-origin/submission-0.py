import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        closest = []

        for point in points:
            x,y = point

            xdist = x*x
            ydist = y*y
            total = xdist + ydist

            heapq.heappush(heap,(total,point))

        for i in range(k):
            temp =  heapq.heappop(heap)
            dist, coord = temp
            closest.append(coord)

        return closest
            