"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.

Example 1:
    Input: "Hello World"
    Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        try:
            if ' ' in s:
                s = s.split(' ')
                return len(s[-1])
            else:
                return len(s)
        except:
            return 0
# Runtime: 28 ms, faster than 60.70% (2020/03/18)
# Memory Usage: 12.8 MB, less than 100.00% (2020/03/18)

