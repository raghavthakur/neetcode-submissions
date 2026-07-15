# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
'''
given a list of words return lists of anagrams

anagrams are words that have the same chars

['x'] -> [['x']]

['cat','atc','dog'] -> [['dog'],['atc', 'cat']]

iterate through the words
sort each of the words
add to hashmap that uses the sorted word as the key and original word as value
return a list of values from the hashmap

runtime: O(n*mlogm) where n is length of string and m is length of avg word
space: O(n*m) storing hashmap of size n and sorted timsort uses size m for aux space

better
since only lowercase letters of words
a -> 0 to z -> 26
iterate through the words
char count in each word using frequency list and use as tuple for hashmap key
if words have the same char count from frequency list then add to hashmap values
return a list of all values from the hashmap
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for word in words:
            # each word can have a count for 26 letters
            count = [0] * 26 # char freq list
            for char in word:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(word) # use dict as count key and original words as value
        
        return list(result.values())
'''
runtime: O(n * m) where n is length of words and m is length of chars in word
space: O(n)
'''







