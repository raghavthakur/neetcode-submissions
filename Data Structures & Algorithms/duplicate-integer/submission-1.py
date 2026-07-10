# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
        
'''
given a list of numbers, return true there is any duplicate in list

numbers not sorted
positive and negative numbers
list can be empty then return false

[1,2,3,3] -> true
[1,2,4,0] -> false

constant lookups -> use a hashmap or set

create set
iterate through the list and add numbers to set
check if number in set then return true
otherwise add to set
return false
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        
        return False

'''
[1,2,3,3] -> true

{1,2,3} -> True

[1,2,4,0]

{1,2,4,0} -> False

[]

{} -> False

runtime: O(n) where n is length of nums
space: O(n) since storing set
'''