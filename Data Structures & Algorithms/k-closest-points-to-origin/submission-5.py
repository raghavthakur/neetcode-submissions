import heapq, math
class Solution:
    # runtime: O(n*logn + k*logn)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []

        for x, y in points:
            # calc euclidean distance
            distance = math.sqrt((x**2 + y**2))

            # add tuple of (distance, x, y) to heap
            heapq.heappush(min_heap, (distance, x, y))

        heapq.heapify(min_heap) # closest distances at top of heap

        while k > 0:
            dis, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1

        return res