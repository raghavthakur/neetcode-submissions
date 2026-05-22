'''
- list is not sorted
- triplets where i + j + k = 0
- indices i, j, k are distinct
- return all triplets with no duplicate triplets

[-1,0,1,2,-1,-4]

[-4,-1,-1,0,1,2]
          i
            j
            k

{(-1,-1,2),(-1,0,1)}
[[-1,-1,2],[-1,0,1]]

returns [[-1,-1,2], [-1,0,1]]

- sort the list
- for each number in the list run two pointers in the sublist to find triplets
- runtime for sorting O(nlogn) and finding triplets is O(n^2)
'''
# Runtime: sorting takes O(nlogn) + O(n^2) + O(n) --> O(n^2)
# Space: O(n) since using set

### Improvements: remove the use of set and skip duplicates using logic since already sorted the list
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # in-place sort
        triplets = [] # distinct triplets

        for i, num in enumerate(nums):
            # skip if num > 0 since no triplets afterwards
            if num > 0:
                break

            # skip duplicate value
            if i > 0 and num == nums[i - 1]:
                continue

            # two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    triplets.append([num, nums[left], nums[right]])
                    
                    # once triplet is found, need to check for remaining triplets
                    # skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                if three_sum > 0:
                    right -= 1
                else:
                    left += 1

        return triplets
        