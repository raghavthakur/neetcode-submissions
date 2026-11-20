'''
assume there is always an answer of pair(i,j)
assume input is not sorted
i cannot be j


[3,4,5,6] target = 7

return [0,1]

[5,5] target = 10
return [0,1]

[4,5,6] target  = 10
return [0,2]

brute:
use two for loops
for each i
then for each j
find a pair i != j that equals to target

runtime: O(n^2) since need to traverse through input twice

better:
sort the input
use binary search to find target
runtime: O(nlogn + logn) -> O(nlogn)

better:
for each number find the compliment = target - num
store number and index in hashmap
if compliment in hashmap then return current index and hashmap index
runtime: O(n)
space: O(n)
'''

# runtime: O(n)
# space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap approach
        hashmap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap and hashmap[comp] != i:
                return sorted([i, hashmap[comp]])

            hashmap[nums[i]] = i # avoid duplicates by checking for comp before updating
            
        return [0,0]

'''
[3,4,5,6] target = 7

{3:0,4:1}

7-3=5
7-4=3


'''
        