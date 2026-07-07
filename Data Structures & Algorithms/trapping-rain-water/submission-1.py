'''
two pointers
left and right
update max height of left
update max height of right
use lowest of both heights
find area inside
increase left
decrease right
'''
class Solution:
    # return the max area between the two bars trapping water
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        max_left_height = 0
        max_right_height = 0

        while left < right:
            # find max height of left
            max_left_height = max(max_left_height, heights[left])

            # find max height of right
            max_right_height = max(max_right_height, heights[right])

            if max_left_height < max_right_height:
                area += max_left_height - heights[left]
                left += 1
            else:
                area += max_right_height - heights[right]
                right -= 1
            
        return area

'''
runtime: O(n) where n is length of list
space: O(1)
'''