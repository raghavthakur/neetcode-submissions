'''
given list of numbers
return list of numbers where num[i] is product of all numbers except num[i]

[1,2,4,6] -> [48,24,12,8]
     i
[1,1,2,8]
[48,24,6,1]

[6*4*2,6*4,6,1] 
[1,1,1*2,1*2*4]

[48, 24, 12, 8]

create a running product list using forward pass
create a running product list using backward pass
create resulting product list from the two lists
return result
'''
class Solution:
    # runtime: O(n) where n is length of nums
    # space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        backward = [1] * len(nums)

        for i in range(1, len(nums)):
            # curr res = prev num * prev res
            forward[i] = nums[i-1] * forward[i-1]

        for j in range(len(nums) - 2, -1, -1):
            backward[j] = nums[j+1] * backward[j+1]

        # can also create new list using list comp and zip()
        for i in range(len(nums)):
            forward[i] = forward[i] * backward[i]

        return forward
