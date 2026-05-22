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
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # in-place sort
        triplets = set() # distinct triplets

        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if num + current_sum == 0:
                    triplets.add((num, nums[left], nums[right]))
                    # once triplet is found, need to check for remaining triplets
                    left += 1
                    right -= 1
                    continue

                if num + current_sum > 0:
                    right -= 1
                else:
                    left += 1

        # convert the set of tuples to a list of lists
        output_list = [list(t) for t in triplets]
        return output_list
        