'''
return length of longest substring without repeating chars

{zxy}
3

"zxyzxyz" -> 3

since zxy

"xxxx" -> 1
since x

assuming:
alphabets only in string
can be a duplicate or no duplicate


seen_char which is dict
window_start=0
window_end
iterate on window_end
add window_end to seen_char
while window_start is in seen_char record max_length and del start from seen_char and increase start

'''
# runtime: O(n) where n is length of s
# space: O(n) since using dict to store substring
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char = {}
        window_start = 0
        max_length = 0

        for window_end in range(len(s)):
            
            # shrink window from start if end in seen_char
            while s[window_end] in seen_char:
                del seen_char[s[window_start]]
                window_start += 1

            seen_char[s[window_end]] = window_end

            # cal window length
            s_length = window_end - window_start + 1
            max_length = max(max_length, s_length)
        
        return max_length
'''
"dvdf" -> 3
    e
  s
 0
 {vdf}
'''

'''
"zxyzxyz" -> 3
    e 
{xyz}
3

abcd -> 4
    e
{abcd}
0

"dvdf" -> 3
   e
'''