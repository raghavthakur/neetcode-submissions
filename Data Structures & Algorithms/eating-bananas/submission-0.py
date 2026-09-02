'''
piles is a list of nums with number of bananas at index i
h is num of hours to eat all bananas

eat bananas per hour k that we choose
each hour choose a pile and eat k bananas from it
cannot eat from another pile in same hour if pile has less than k bananas

return min k to eat all bananas in h hours

Input: piles = [1,4,3,2], h = 9

Output: 2


want to reduce nums to 0 with smallest k rate while reducing h until 0
start k rate from largest number in nums list
then try to min k


choose some k and optimize it
choose starting k to be largest value in nums list
if reducing val in nums list to 0 results in an h > 0 then reduce k and try again

list is not sorted
sort list
[1,2,3,4] h = 9
l
       r

[4,10,23,25], h = 4
          l
          r

[1,2,3,4,5,6,7,8,9,10...,25]


find k and k can be at most the largest value in the list
use binary search from k = 1 to k = max(nums)
test if selected k is valid
iterate through the nums
reduce nums val by k until val <= 0 while h > 0
if finish nums interation and h >= 0 then update min k
if do not finish nums and break out of loop since h < 0 then find new k
'''

class Solution:

    # runtime: O(n*logm) where n is size piles list and m is max number in piles
    # space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def validate_k(k):
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)
            
            return hours_needed <= h

        left = 1
        right = max(piles)

        min_k = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if validate_k(mid):
                min_k = min(min_k, mid)
                # decrease k
                right = mid - 1
            else:
                # increase k
                left = mid + 1
        
        return min_k

'''
[1,2,3,4] h = 9
 m
l=1
r=1
min_k=2

[-3,0,-1,0] c = 3
'''



        