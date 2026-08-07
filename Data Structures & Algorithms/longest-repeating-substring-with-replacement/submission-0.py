'''
string s and number k
s has only uppercase letters
can replace k chars in string
return length of substring with only one distinct char

"XYYX" k=2 -> replace X with Y
-> "YYYY"
output=4

"AAABABB" k=1 -> replace A with B or B with A
-> "AAABA" -> "AAAAA"
output=5

{A:4,B:1}

track the char freq and choose the smallest freq to replace with k

window_start
char_freq dict
window_end
max_length
iterate using window_end throuhg list
add char and freq to dict
for given window replace char with most freq char
num of replacements = window_size - freq of most freq char in window
update max_length if num_replacements > k
increase window_start
return max_length

'''
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        max_length = 0
        char_freq = defaultdict(int)

        for window_end in range(len(s)):
            char_freq[s[window_end]] += 1

            # find freq of most freq char in window
            window_size = window_end - window_start + 1
            max_freq_char = max(char_freq.values())
            num_rep = window_size - max_freq_char
            
            if num_rep > k:
                char_freq[s[window_start]] -= 1
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
            
'''
"AAABABB" k=1 -> replace A with B or B with A
  s
      e
-> "AAABA" -> "AAAAA"
output=5

ws=6
ml=0
{A:3,B:2}
'''



