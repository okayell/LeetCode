"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
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