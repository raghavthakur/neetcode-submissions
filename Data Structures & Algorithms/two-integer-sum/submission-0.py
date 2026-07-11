# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

'''
given list of numbers and target return index i and index j
such that nums[i] + nums[j] == target and i != j

always one pair that meets condition
return list with smallest index first
list is not sorted
list can have duplicates


[3,4,5,6], target=7 -> [0,1]

[5,5], target=10 -> [0,1]

x + y = z
y = z - x

find the compliment which is target - num in the list and return their indices

create a hashmap of the list and indices
iterate through the list and find the compliment = target - current
find the compliment in the hashmap and return both current index and hashmap index such that indices do not equal

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]

        index_map = {}
        for i in range(len(nums)):
            index_map[nums[i]] = i

        for j in range(len(nums)):
            comp = target - nums[j]
            if comp in index_map and index_map[comp] != j:
                if index_map[comp] < j:
                    result[0], result[1] = index_map[comp], j
                else:
                    result[0], result[1] = j, index_map[comp]

        return result

'''
runtime: O(n) where n is list of nums with two passes
space: O(n) since using dict to store nums and indices
'''
