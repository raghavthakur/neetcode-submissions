'''
nums sorted in increasing order
no duplicates
target

search for target within nums and return target index
otherwise return -1

assume runtime should be O(logn) --> binary search

nums = [-1,0,2,4,6,8], target = 4
return 3

nums = [-1,0,2,4,6,8], target = 3
return -1

left
right
while left < right
mid = left + right // 2
if mid val == target val return target index
if mid val > target then move right by mid - 1
if mid val < target then move left by mid + 1
return -1
'''
class Solution:
    # runtime: O(logn) since search list by half on each iteration
    # space: O(1) no extra space
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
        
'''
nums = [-1,0,2,4,6,8], target = 4
return 3

l=3
r=5
mv=4
'''