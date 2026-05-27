'''
bar:     0  1  2  3
height: [0, 4, 1, 2]

choose any two bars that gives max container of water
left has to be max
right has to be max
spread in between to calc volume = min height x width to find max volume

- two pointers
- left pointer
- right pointer
- cal the distance between the two pointers to cal max volume and update max volume
- max volume = min of two pointers x distance between two pointers (r - l)
- move either pointer that is the smallest of the two
- return max volume which is min pointer height x distance between pointers


[1,7,2,5,4,7,3,6] --> 7 length
   l
   r

mv=36

[2,2,2]
 l
   r

mv=4
'''
# Runtime: O(n) where n is length of heights
# Space: O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = 0

        while left < right:
            # calc max volume
            max_vol = max(max_vol, min(heights[left], heights[right]) * (right - left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_vol