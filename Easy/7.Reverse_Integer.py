class Solution:
    def reverse(self, x):
        if x > 2**31-1 or x <= -2**31:
            return 0
        if x < 0:
            r = int('-' + str(int(str(x).strip('-')[::-1])))
        else:
            r = int(str(x)[::-1])
        if r > 2**31-1 or r <= -2**31:
            return 0
        return r
# Runtime: 24 ms, faster than 93.75% (2020/02/20)
# Memory Usage: 12.7 MB, less than 100.00% (2020/02/20)
