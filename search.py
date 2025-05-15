from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        for i in range(len(nums)):
            if (target == nums[i]):
                start = i
                break
        for i in range(len(nums)-1,-1,-1):
            if(target == nums[i]):
                end = i
                break
                
        return [start , end]
sol = Solution()
nums = [5,7,7,8,8,10]
target = 8
nums1 = [1]
target1 = 1
print(sol.searchRange(nums,target))
print(sol.searchRange(nums1,target1))