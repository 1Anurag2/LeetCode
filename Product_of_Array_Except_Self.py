class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # Prefix product
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

sol = Solution()
arr = [1, 2, 3, 4]
print(sol.productExceptSelf(arr)) 
