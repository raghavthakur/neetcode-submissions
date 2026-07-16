# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
'''
given list of numbers nums and number k return the k most frequent number

[1,2,2,3,3,3] k=2 ->[2,3]
return two of the most frequent numbers

[7,7] k=1 -> [7]
return one of the most frequent numbers


use hashmap to count the number of repeated values
key as the number
value as the count
sort the hashmap based on count
return k number of keys from the hashmap that has most frequent values at the start
'''
from collections import defaultdict
import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        # sort the hashmap from it's values in decreasing order
        sorted_values = dict(sorted(freq_map.items(), key=operator.itemgetter(1)))

        value_iterator = iter(reversed(sorted_values))

        for i in range(k):
            result.append(next(value_iterator))

        return result

'''
runtime: O(nlogn)
space: O(n)
'''
