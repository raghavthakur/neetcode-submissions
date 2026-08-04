'''
find length of longest substring without duplicate char

"dvdf" -> 3
 s
 e
 {}

sliding window
window_start = 0
longest_substring_length
seen_set
window_end iterate through s
check if window_end in seen_set
remove window_start from seen_set
increase window_start

add window_end to seen_set
calc window_length as longest_substring_length

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen_set = set()

        for right in range(len(s)):
            # remove duplicate from set
            while s[right] in seen_set:
                seen_set.remove(s[left])
                left += 1

            # add current to set
            seen_set.add(s[right])

            # cal window length as max_substring_length
            max_length = max(max_length, right - left + 1)

        return max_length
            
        