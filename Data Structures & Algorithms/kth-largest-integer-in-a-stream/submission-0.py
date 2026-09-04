'''
stream of ints
stream is not sorted
find kth largest int

[1,2,3,3] k=3
3rd largest int is 3
add 3 [1,2,3,3,3] return 3
add 5 [1,2,3,3,3,5] return 3
add 6 [1,2,3,3,3,5,6] return 3
add 7 [1,2,3,3,3,5,6,7] return 5 since 5 is 3rd largest int

initialize k and list of nums
create a max heap
heapify nums
then return the kth value from the heap
'''
import heapq
class KthLargest:

    # runtime: O(m * log k) where k is size of heap and m is number of calls to add
    # space: O(k)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) # takes O(logk) for heap size k
        # maintain heap size of k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap) # takes O(logk) for heap size k
        return self.heap[0] # O(1)
        
'''
[1,2,3,3] k=3

                        
heap = [-8-7,-6,-5,-3,-3,-3,-2,-1]
add(8)
add(7)
add(6)
add(5)
add(3)
'''