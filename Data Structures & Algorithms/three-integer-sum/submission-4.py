'''
list of numbers
find 3 numbers that sum to 0
find all triplets
no duplicate triplets
return a list of triplets which is list of lists

assume list is not sorted
assume may not be a solution then return []

[-1,0,1,2,-1,4] -> [[-1,-1,2],[-1,0,1]]

[0,1,1] -> []

brute
3 loops that checks for triplets
runtime: O(n^3)

better
sort list -> O(nlogn)
[-1,-1,0,1,2,4]
  i
    j
             k
iterate through the list one by one element with i
two pointers j and k to find two numbers that i - (j+k) sum 0
create another function that performs two pointers
left
right
while left < right
i + j + k == 0
-i = j + k
if i - (left + right) == 0
if left + right < i then increase left
if left + right > i then decrease right
need find all triplets so once answer is found, continue with rest of list until j not < k
check if triplet is distinct
add triplet to result list as triplet
return result list

runtime: n*n + nlogn --> O(n^2)
space: O(1)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums list in-place
        nums.sort() 

        result = []

        for i in range(len(nums) - 2): # don't want to reach last two numbers
            # since list is sorted I can skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue # to the next element

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # find sums that == target
                pair_sum = nums[left] + nums[right]
                
                if pair_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # NOTE: should we continue to find more pairs? YES

                    # skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # skip duplicates for right
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                if pair_sum < target:
                    left += 1
                else:
                    right -= 1


                # NOTE: add distinct triplet to result and prevent duplicate numbers

        return result
    
'''
[-1,0,1,2,-1,4] -> [[-1,-1,2],[-1,0,1]]
         
         s
[-1,-1,0,1,2,4]
         i
           l
           r
target=1

2,3,0,1

[[-1,-1,2],[-1,0,1]]

runtime: O(n^2) where n is length of nums
space: O(1)
'''