class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
# Runtime: 100 ms, faster than 35.28% (2020/02/20)
# Memory Usage: 14.5 MB, less than 97.54% (2020/02/20)
