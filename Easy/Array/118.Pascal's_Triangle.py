"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        p = [[1]]
        for i in range(1, numRows):
            l = list()
            l.append(1)
            t = 0
            i -= 1
            while t < i:
                l.append(p[i][t] + p[i][t+1])
                t += 1
            l.append(1)
            p.append(l)
        return p
# Runtime: 32 ms, faster than 25.96% (2020/02/24)
# Memory Usage: 12.8 MB, less than 100.00% (2020/02/24)


class Solution_2:
    def generate(self, numRows: int) -> List[List[int]]:
        p = []
        for n in range(numRows):
            row = [None for i in range(n+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = p[n-1][j-1] + p[n-1][j]
            p.append(row)
        return p
# Runtime: 28 ms, faster than 68.14% (2020/02/24)
# Memory Usage: 12.8 MB, less than 100.00% (2020/02/24)


