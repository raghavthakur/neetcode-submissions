'''
each row is sorted increasing order
first int of every row is greater than last int of prev row

return true if target is in matrix
otherwise return false

Input: matrix = [

[1,2,4,8], # top row
[10,11,12,13],
[14,20,30,40] # bottom row

], target = 10
Output: true

run binary search on rows
top and bottom rows
mid row = (top + bottom) // 2
if target > matrix[mid][-1] then move down so top = mid + 1
if target < matric[mid][0] then move up so bottom = mid - 1
else break and run second binary search on the cols
if not (top <= bottom) return false

run binary search on cols
left and right for nums in col
'''
class Solution:

    # runtime: O(log(n*m)) where n is num of rows and m is num cols
    # space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])

        def binary_search(nums):
            # binary search on the cols
            left = 0
            right = COL - 1

            while left <= right:
                mid = (left + right) // 2

                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    return True
            
            return False


        top = 0
        bottom = ROW - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target > matrix[mid_row][-1]: # rows last element
                top = mid_row + 1 # move top down
            elif target < matrix[mid_row][0]: # rows first element
                bottom = mid_row - 1 # move bottom up
            else:
                return binary_search(matrix[mid_row])

        return False
        