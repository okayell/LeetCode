class Solution:
    def isPalindrome(self, x):
        a = list(str(x))
        if a[::-1] == a:
            return True
        else:
            return False
# Runtime: 48 ms, faster than 93.49% (2020/02/20)
# Memory Usage: 12.7 MB, less than 100.00% (2020/02/20)


class Solution_2:
    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)
# Runtime: 52 ms, faster than 86.68% (2020/02/20)
# Memory Usage: 12.8 MB, less than 100.00% (2020/02/20)
