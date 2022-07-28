"""
Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if n + nums[j] == target:
                    return [i, j]
# Runtime: 4884 ms, faster than 19.04% (2020/02/20)
# Memory Usage: 13.6 MB, less than 92.33% (2020/02/20)



