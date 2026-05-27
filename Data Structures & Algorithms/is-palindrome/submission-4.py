'''
- ignores alphanumeric chars isalnum
- is case insensitve


"Was it a car or a cat I saw?"
->
"wasitacaroracatisaw" 
- include capital and non-cap chars and numbers
- ignore spaces and special chars


- two pointers
- left and right
- iterate through the list while left < right
- check if char isalnum and if so then compare lowercase letters
- if chars don't match then return false
- if not alnum then we can skip char
- return true


"1Was it a car or a cat I saw?1"
               l
               r


'''

# Runtime: O(n) where n is size of s
# Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum(): # don't forget index out of range
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # chars are alnum
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True