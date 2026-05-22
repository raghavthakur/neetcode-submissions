'''
- non-decreasing order
- return indices
- index1 < index2 and both sum to target
- cannot use same element twice
- index starts at 1 (not 0)


[1,2,3,4] target=3
return [1,2] that sums to 3

- two pointers, left and right
- while left < right
- sum left and right
- check if larger than target, decrease right
- check if smaller than target, increase left
- if both sum to target then return 1 based indices
'''
# Runtime: O(n) where n is size of numbers
# Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum_value = numbers[left] + numbers[right]
            if sum_value == target:
                return [left + 1, right + 1] # 1 based indices
            
            if sum_value > target:
                right -= 1
            else:
                left += 1
        
        # expected to always return 1 solution
        return [-1, -1]

'''
[1,2,3,4] target=3
 l
   r

[1,2]
'''

        