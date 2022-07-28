"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples1:
    s = "leetcode"
    return 0.
Examples2:
    s = "loveleetcode",
    return 2.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] += 1
            if c not in d:
                d[c] = 1

        l = list()
        for c in s:
            if d[c] == 1:
                l.append(s.index(c))
        if l == []:
            return -1
        return min(l)
# Runtime: 168 ms, faster than 21.77% (2020/02/24)
# Memory Usage: 12.9 MB, less than 100.00% (2020/02/24)


class Solution_2:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            if c not in d:
                d[c] = 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
# Runtime: 136 ms, faster than 39.76% (2020/02/24)
# Memory Usage: 12.7 MB, less than 100.00% (2020/02/24)

# -------------------------------------------------------------
from collections import defaultdict


def zero():
    return 0


class Solution_3:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(zero)
        for c in s:
            d[c] += 1
        for i, c in enumerate(s):
            if d[s[i]] == 1:
                return i
        return -1
# Runtime: 112 ms, faster than 60.76% (2020/02/24)
# Memory Usage: 12.6 MB, less than 100.00% (2020/02/24)
