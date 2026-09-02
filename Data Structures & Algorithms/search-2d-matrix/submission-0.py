'''
grid of mxn
target
row sorted in increasing order
first int in row is always greater then last in prev row

return true if target in matrix
otherwise return false

solution must be in O(log(m * n))

iterate each row then inside row loop run binary search to find target
return true if target found

after grid iteration return false

runtime: n*logm
hint: first int in row is always greater then last int in prev row
use binary search for row iteration for row_1[0], row_2[0], row_3[0] and check for target in those ranges
                    0           mid           len(row)-1
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
                 r         r             r
'''
class Solution:

    # runtime: O(log n * log m) --> O(log(n * m)) where n is rows and m is col
    # space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])

        def binary_search(nums):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2 # to prevent overflow

                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False

        left = 0
        right = ROW - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if binary_search(matrix[mid]):
                    return True

            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        # target not found in matrix
        return False
        