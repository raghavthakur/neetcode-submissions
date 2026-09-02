'''
piles is list of ints
h is number of hours
find k which is speed
need to finish pile with k for each hour and cannot move to next int in same hour

val / speed (val per time) = time taken to eat

return min k to eat all values within h hours

piles = [1,4,3,2], h = 9

max speed can be max value in piles --> max(piles)
find min speed so speed can range from 1 to max(piles)
since range is in increasing order we can use binary search to find min speed

brute force
iterate through list and reduce each value in list by speed k until 0
record speed k if time taken in hours <= hours h
repeat iteration for each value of speed k and increasing it by 1 to max(list value)
runtime: O(n * m) where n is size of list piles and m is range from 1 to max(val) in list piles
space: O(1)

better
use binary search from 1 to max(piles) to find speed k
for each speed k iterate through list piles and for each value find time taken to eat = val / speed k
if time taken <= hours h then update min_k and decrease speed
if time taken not <= hours h then increase speed
return min_l
runtime: O(logn * m)
space: O(1)

piles = [1,4,3,2], h = 9

[1,2,3,4]
 l
   m
        r

[1,4,3,2] k=2 h=9
       i
total_hours+=ceil(val/k)
th=6
6 <= 9 so update min_k to be 2 and continue binary search

'''
import math
class Solution:
    # runtime: O(m * logn) where m is size of list piles and n is range of k from 1 to max(piles)
    # space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def test_k(speed):
            total_time = 0
            
            for val in piles:
                total_time += math.ceil(val / speed)
            
            return total_time <= h

        # binary search to find best k
        left = 1
        right = max(piles)

        min_k = max(piles)

        while left <= right:
            k = (left + right) // 2
            # test the k on the list
            if test_k(k):
                # update k and decrease k
                min_k = min(min_k, k)
                right = k - 1
            else:
                # k not valid so increase k
                left = k + 1
        
        return min_k













