'''
list of words that we want to group togather for anagrams

use a dict
iterate the list of words
for each word we can sort the word and create a sorted word
use a dict and use the sorted word as a key and the original word as the value
return list of the dict
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list) # initialize the dict as a list using defaultdict

        for word in strs:
            sorted_word = "".join(sorted(word)) # ex. eat and ate becomes aet

            anagram_group[sorted_word].append(word)

        return list(anagram_group.values())

'''
Runtime: O(n * mlogm) where n is length of strs and m is length of each word in strs
Space: O(n * m) where m is longest string and n is number of strings
'''