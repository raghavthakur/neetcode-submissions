'''
list of numbers sorted in non-decreasing order
return (1-index based) indices of two numbers that sum to target
index1 < index2
cannot use same element twice
[numbers], target -> [indices]

ex. [1,2,3,4] target=3 -> [1,2] indices that sum to 3
     l
       r

solution:
two pointers
left
right
while left < right
sum = left + right
if sum == target then return indices
if sum < target then increase left
if sum > target then decrease right
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]

            if two_sum == target:
                return [left + 1, right + 1] # 1 based indices
            
            if two_sum < target:
                left += 1
            else:
                right -= 1
        
        return

'''
runtime: O(n) where n is size of numbers
space: O(1)
'''