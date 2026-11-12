'''
two strings s and t
return true if s and t is anagram of each other

anagram is strings with same chars and same chars frequency

"racecar", "carrace"
return true

"jar", "jam"
return false

"x", "x"
return true

"", ""
return true

create chars_freq map of first string
iterate through second string and remove matching chars from char_freq map
if char is not in char_freq map then return False

if len char_freq map is not 0 then return False else return True
'''
# runtime: O(s + t) where s and t are length of s, t strings
# space: O(s)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = {}

        for char in s:
            if char not in char_freq:
                char_freq[char] = 1
            else:
                char_freq[char] += 1
        
        for char in t:
            if char not in char_freq:
                return False
            char_freq[char] -= 1

            if char_freq[char] == 0:
                del char_freq[char]

        return len(char_freq) == 0

'''
s = "racecar", t = "carrace"

{r: 0, a: 0, c: 0, e: 0}


'''