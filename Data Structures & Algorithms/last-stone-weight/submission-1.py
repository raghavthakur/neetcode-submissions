'''
each step choose two largest values
if x == y both stones destroyed
if x < y stone x is destroyed and y has new value y - x
continue until only one stone left
return weight of last stone or 0 if none left

assuming no negative value or 0 value for weights in stones

[2,3,6,2,4]
choose 6 and 4, remove 4 and add 2
[2,3,2,2]
choose 3 and 2, remove 2 and add 1
[2,2,1]
choose 2 and 2, remove both
[1]
return 1

brute force
[2,3,6,2,4] --> [2,2,3,4,6]
sort the list
pop last two values
cal diff and add remaining value
repeat until only 1 value left or none

sort list then pop then add then sort list then repeat
need to sort m times until list len is 1 or 0
runtime: O(m*nlogn)

use a max heap after heapify O(n)
pop of two values from the top O(logn)
add diff value to heap O(logn)
repeat
runtime: O(nlogn) where n is size of heap

'''
import heapq

# runtime: O(n * logn) where n is the size of the heap which is len of stones
# space: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [x * -1 for x in stones] # O(n)
        heapq.heapify(max_heap) # O(n)

        # O(n)
        while len(max_heap) > 1:
            first_val = heapq.heappop(max_heap) * -1 # O(logn)
            second_val = heapq.heappop(max_heap) * -1 # O(logn)

            # compare values
            if first_val == second_val:
                continue
            else:
                diff = abs(first_val - second_val)
                heapq.heappush(max_heap, diff * -1) # O(logn)
        
        if max_heap:
            return max_heap[0] * -1
        
        return 0

'''
[2,3,6,2,4]

    -1

pop [-6,-4]
add -2

pop [-3,-2]
add -1

pop [-2,-2]

return 1
'''


        