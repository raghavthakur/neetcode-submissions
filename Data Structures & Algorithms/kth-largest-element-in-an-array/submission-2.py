'''
use min heap
'''
import heapq
class Solution:
    # runtime: O(n * log k) where n is size of list and k is size of heap
    # space: O(k) where k is size of heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [] # smallest value at root

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                # remove smallest value so heap has k largest elements
                heapq.heappop(min_heap)
        
        return min_heap[0]

'''
[2,3,1,5,4], k = 2

                4 
                   5
'''

        