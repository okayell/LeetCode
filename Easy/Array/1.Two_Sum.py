"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if n + nums[j] == target:
                    return [i, j]
# Runtime: 4884 ms, faster than 19.04% (2020/02/20)
# Memory Usage: 13.6 MB, less than 92.33% (2020/02/20)


class Solution_2:
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
# Runtime: 44 ms, faster than 92.42% (2020/02/20)
# Memory Usage: 14.2 MB, less than 58.6% (2020/02/20)


class Solution_3:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in d:
                return [d[t], i]
            else:
                d[nums[i]] = i
# Runtime: 40 ms, faster than 97.98% (2020/02/24)
# Memory Usage: 14.4 MB, less than 41.16% (2020/02/24)

