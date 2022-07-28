"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2
Example 2:
    Input: [1,3,5,6], 2
    Output: 1
Example 3:
    Input: [1,3,5,6], 7
    Output: 4
Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target not in nums:
                if n > target:
                    return i
            if n == target:
                return i
        return len(nums)
# Runtime: 444 ms, faster than 5.23% (2020/02/24)
# Memory Usage: 13.4 MB, less than 100% (2020/02/24)


class Solution_2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if target <= num:
                return index
        return len(nums)
# Runtime: 52 ms, faster than 42.64% (2020/02/24)
# Memory Usage: 13.4 MB, less than 100% (2020/02/24)