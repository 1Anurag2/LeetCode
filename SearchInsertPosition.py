from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        last_item = nums[n-1]

        for i in range(n):
            if(target == nums[i]):
                return i
            elif(target < nums[i]):
                return i
            elif(target > last_item):
                return n

sol = Solution()
nums = [1]
target = 0
nums1 = []
print(sol.searchInsert(nums , target))          
             

            
