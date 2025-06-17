from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        sorted_nums = sorted(nums)
        for i in range(length):
            if (i != sorted_nums[i]):
                return i
        return length