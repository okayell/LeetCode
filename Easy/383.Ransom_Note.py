"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines;
otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
"""


class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        l = list(m)
        for c in r:
            if c in l:
                l.remove(c)
            else:
                return False
        return True
# Runtime: 48 ms, faster than 71.36% (2020/02/24)
# Memory Usage: 13.1 MB, less than 100.00% (2020/02/24)



