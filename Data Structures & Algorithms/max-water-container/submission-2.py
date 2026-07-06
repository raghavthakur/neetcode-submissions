# class Solution:
#     def maxArea(self, heights: List[int]) -> int:

'''
given list of heights and return max amount of water container can store
find the max height between left bar and right bar
then multiple that by the distance between two bars
area = length x height

[1,7,2,5,4,7,3,6] -> 36 since left=7 and right=6 then * distance of 6
   l
             r
mw=36
distance= r-l

two pointers
left
right
max_water
while left < right
use the smaller of the two heights * distance between left and right
update max_water
TODO: check if left or right is lower of the two heights and move the lower over
return max_water
'''

class Solution:
    # Returns max water in container
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        water_level = 0

        while left < right:
            # find smallest height
            if heights[left] < heights[right]:
                water_level = heights[left] * (right - left)
            else:
                water_level = heights[right] * (right - left)
            max_water = max(max_water, water_level)

            # move the lower of the two heights to next index
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water

'''
[1,7,2,5,4,7,3,6] -> 36
   l
               r

mw=7
wl=

runtime: O(n) where n is length of list
space: O(1)
'''