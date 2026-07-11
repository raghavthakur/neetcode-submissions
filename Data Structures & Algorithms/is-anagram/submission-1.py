# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
'''
given two strings return true if two strings are anagrams otherwise return false

exact same chars in two strings
number of chars same in two strings
orders can be different

"racecar", "carrace" -> true

"jar", "jam" -> false

strings cannot be empty
strings have only lowercase letters

if two strings length is diff then return false
char count of first string
reduce char count from second string
if char count is not empty or has some length then return false
use dict
add to dict by iterating first string
remove to dict by iterating second string
'''
class Solution:
    def isAnagram(self, string_one: str, string_two: str) -> bool:
        # lengths diff
        if len(string_one) != len(string_two):
            return False

        # iterate through string 1
        char_count = {}
        for char in string_one:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1

        # iterate through string 2
        for char in string_two:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        
        return len(char_count) == 0

'''
"racecar", "carrace" -> true
  i
             j

{} -> True

runtime: O(n + m) where n is len of string 1 and m is len of string 2
space: O(n) -> this is wrong because only 21 chars so should be O(1) space

need to do better: O(1) space
strings immutable cannot sort
'''



