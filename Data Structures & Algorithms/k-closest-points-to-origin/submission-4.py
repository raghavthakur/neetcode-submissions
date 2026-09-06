'''
points[i] = [xi, yi]

return the k closest point to origin [0,0]

distance between points = sqrt((x1 - x2)**2 + (y1 - y2)**2)

points = [[0,2],[2,2]], k = 1

origin = [0, 0]
find distance between origin and points
[0, 2], [2, 2]
return k=1 closest distance to origin
return [0, 2]

points = [[0,2],[2,0],[2,2]], k = 2

return [0,2], [2,0]

brute force
sort each point in decreasing order and return k points from end of list
runtime: O(n * nlogn)

better
create a min heap
iterate through each point and calc ecludian distance from origin
map ecludian distance value to point tuple in hashmap
add ecludian distance value to min heap and maintain size k

return points from hashmap using k heap values and return as list
'''
import math, heapq

# runtime: O(n*logn) where n is length of points
# space: O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            e_dist = math.sqrt(x**2 + y**2)
            # edge case if two diff points have same ecludian distance


            heapq.heappush(max_heap, (-e_dist, x, y)) # store tuple in heap

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        # extract point from tuples in heap
        return [[x, y] for (e_dist, x, y) in max_heap]

'''
bug for edge case: two diff points have same ecludian distance

TEST
points = [[0,2],[2,0],[2,2]], k = 2
           x y

               


mh = []
dp = {e1: [0,2], e2: [2,0], e3: [2,2]}
res = [[0,2], [2,0]]
'''
        