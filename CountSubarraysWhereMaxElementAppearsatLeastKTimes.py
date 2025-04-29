from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxElement = max(nums)
        total_subarray = n*(n+1)//2
        left = right = Count = freq = 0
        for right in range(n):
            if(nums[right] == maxElement):
                freq += 1
            
            while(freq >= k):
                if(nums[left] == maxElement):
                    freq -= 1
                left += 1
            
            Count += right - left + 1
        return total_subarray - Count

sol = Solution()
nums = [1,3,2,3,3]
k = 2 
print(sol.countSubarrays(nums,k))