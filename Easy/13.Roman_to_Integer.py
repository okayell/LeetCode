class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i > 0 and d[s[i-1]] < d[s[i]]:
                sum += (d[s[i]] - d[s[i-1]] - d[s[i-1]])
            else:
                sum += d[s[i]]
        return sum
# Runtime: 40 ms, faster than 88.21% (2020/02/20)
# Memory Usage: 12.8 MB, less than 100.00% (2020/02/20)