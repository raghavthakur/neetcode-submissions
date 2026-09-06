'''
find kth largest int in stream of values

ex. k = 2 [1,2,3,3] return 2
ex. k = 3 [1,2,3,3] return 1

assume stream is not sorted

use a min heap of size k
push and pop to heap is O(logn) and getting heap value at index 0 is O(1)

                    1
                2      3
                         3

                    if k = 2

                    2
                       3

'''
import heapq

# total runtime is O(m * logn) in the worst case where m is number of times add is called 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) # heapify into a min heap O(n)

        # maintain a heap of size k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
    # runtime: O(logn) to add and to maintain heap m * O(logn) since can call add m times
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # maintain a heap of size k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0] # return the kth largest heap
