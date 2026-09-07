'''
unsorted nums and int k
return kth largest num in list
kth largest in sorted order

[2,3,1,5,4] k = 2
[1,2,3,4,5]
return 4

solve without sorting

brute force
sort the list and return kth number (len(n) - k)

assume there can be duplicates
assume there are no negatives

[2,3,1,1,5,5,4] k = 3
return 4

better
use a max heap to keep largest element at top and return kth number
create a heap with negative values from nums
pop off values from heap k times
return value
'''
import heapq
class Solution:
    # runtime: O(n*logn + k*logn)
    # space: O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [] # largest value at root

        for num in nums:
            heapq.heappush(max_heap, num * -1)
        
        # heap has k elements
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        
        return max_heap[0] * -1

'''
[2,3,1,1,5,5,4] k = 3
return 4

[-4,-3,-2,-1,-1]
'''



        