'''
return true or false if any value appears more than once in the list

in: [1,2,3,3]
out: True

in: [1,2,3,4]
out: False

assume the list is sorted order?
assume the list has negative and positive numbers?

use a set to store numbers from the list
if number is in set then return True
runtime: O(n) since iterate through list and store each number in set
set lookup is constant time
space: O(n) since storing set

alternative
sort the list O(nlogn) time
iterate through the list and check if prev number == current O(n)
total runtime: O(nlogn)
space: O(1) if using in-place sort
'''

# runtime: O(n) where n is length of list nums
# space: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True # duplicate found
            num_set.add(num)

        return False

'''
in: [1,2,3,3]
           i
out: True

{1,2,3}
return True
'''