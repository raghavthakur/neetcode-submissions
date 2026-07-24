'''
encode a list of strings to a string that sends to decode
decode a string back into the list of strings

encode: [""] -> ""
decode: "" -> [""]

encode: ["Hello", "World"] -> "Hello,//World"
deconde: "Hello,//World" -> ["Hello", "World"]

encode
use a special char to denote where to split the string on
result string
iterate through list of strings
for each string append to result string and append // afterwords if not last string
return result string

decode
string.split on //
return list of strings

'''
class Solution:
    def encode(self, strs: List[str]) -> str:
        # add length of word in front of string
        # add delimiter # after word

        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string
        
        return result # "5#Hello5#World"

    def decode(self, string: str) -> List[str]:
        res = []
        i = 0

        # for each word read the length unitl #
        while i < len(string):
            j = i
            while string[j] != '#':
                j += 1
            length = int(string[i: j])
            word = string[j + 1: j + 1 + length]
            res.append(word)
            i = j + 1 + length
        
        return res

'''
"5#Hello5#World"
        i
  j
[]
length=5
word=Hello

for both encode and decode
runtime: O(n) where n is length of string
space: O(m) where m is length of word from string slicing
'''



