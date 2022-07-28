"""
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t.
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    s = "abc", t = "ahbgdc"
    Return true.
Example 2:
    s = "axc", t = "ahbgdc"
    Return false.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        n = 0
        for i in t:
            if i == s[n]:
                n += 1
                if n == len(s):
                    return True
                continue
        return False
# Runtime: 104 ms, faster than 75.83% (2020/02/24)
# Memory Usage: 17.4 MB, less than 26.67% (2020/02/24)


class Solution_2:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(item in t for item in s)
# Runtime: 60 ms, faster than 82.3% (2020/02/24)
# Memory Usage: 17.2 MB, less than 26.67% (2020/02/24)