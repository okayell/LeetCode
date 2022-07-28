class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)
# Runtime: 32 ms, faster than 58.82% (2020/02/20)
# Memory Usage: 12.7 MB, less than 100% (2020/02/20)
