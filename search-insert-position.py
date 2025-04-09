class Solution:
    def findindex(self,nums,target):
        self.target = target
        self.nums = nums

        for i in range(len(nums)):
            if(nums[i] >= target):
                return i
        return len(nums)

sol = Solution()
nums1 = [1,3,5,6]
print(sol.findindex(nums1,5))

nums2 = [1,3,5,6]
print(sol.findindex(nums2,2))

nums3 = [1,3,5,6]
print(sol.findindex(nums3,7))