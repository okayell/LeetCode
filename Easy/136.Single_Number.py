"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1
Example 2:
    Input: [4,1,2,1,2]
    Output: 4
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n not in nums[:i] and n not in nums[i+1:]:
                return n
# Runtime: 5060 ms, faster than 5.02% (2020/02/24)
# Memory Usage: 15.2 MB, less than 9.84% (2020/02/24)


class Solution_2:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        return l[0]
# Runtime: 1228 ms, faster than 8.42% (2020/02/24)
# Memory Usage: 15.2 MB, less than 13.12% (2020/02/24)


class Solution_3:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
# Runtime: 84 ms, faster than 85.88% (2020/02/24)
# Memory Usage: 15.1 MB, less than 19.67% (2020/02/24)
