'''
String -> Bool
return true if given string is a palindrome
ignore non alphanumeric chars such as space and special characters
handle upper and lowercase letters
string has to be same forward as is backwards

ex. "Was it a car or a cat I saw?" -> true
ex. "tab a cat" -> false

solution
use two pointers
left and right
while left < right
if either left or right is a space or special char then continue
if letter or number then check if letter and convert to lowercase to compare
if chars mismatch then return false
reach end of string and return true
'''

class Solution:
    def isPalindrome(self, words):
        left = 0
        right = len(words) - 1

        while left < right:
            # skip spaces and special chars
            while left < right and not words[left].isalnum():
                left += 1
            while right > left and not words[right].isalnum():
                right -= 1
            
            # handle numbers and uppercase letters
            if words[left].lower() != words[right].lower():
                return False

            left += 1
            right -= 1
        
        return True
            
'''
"Was it a car or a cat I saw?" -> true
              l
                r

runtime: O(n) where n is length of words
space: O(1)
'''

